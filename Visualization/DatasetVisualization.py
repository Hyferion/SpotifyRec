import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def scatter_plot_two_features(dataset, features):
    """Creates a scatter plot for two features. Good for finding correlation between features.
    Parameters:
    dataset (dataframe): dataframe containing the whole dataset

    features (list): list of strings containing the name of the features

    Returns: none

    """
    colors = {True: 'g', False: 'r'}
    fig, ax = plt.subplots()

    for i in range(len(dataset[features[0]])):
        ax.scatter(dataset[features[0]][i], dataset[features[1]][i], color=colors[dataset['liked'][i]])
    ax.set_title(features[0] + " -- " + features[1])
    ax.set_ylabel(features[0])
    ax.set_xlabel(features[1])
    ax.grid(True)
    plt.show()


def histo_plot_frequency(dataset, feature):
    """Histogramm which shows the distribution of a feature. How many songs are present with this value
    Parameters:
    dataset (dataframe): dataframe containing the whole dataset

    feature (string): string containing the feature to plot

    Returns: none

    """
    fig, ax = plt.subplots()

    ax.hist(dataset[feature].to_string())
    ax.set_title('Number of Songs -- ' + feature)
    ax.set_xlabel(feature)
    ax.set_ylabel('Number of Songs')
    plt.show()


def bar_plot_multiple_features(dataset):
    """Creates a bar plot with multiple groups based on features, for every group two bars are created (liked,
    disliked)

    Parameters:
    dataset (dataframe): dataframe containing the whole dataset

    Returns: none
    """
    fig, ax = plt.subplots()

    features = ['acousticness', 'energy', 'danceability', 'instrumentalness']

    trues = dataset.loc[dataset['liked'] == True]
    falses = dataset.loc[dataset['liked'] == False]

    features_trues = []
    features_falses = []

    for feature in features:
        features_trues.append(trues[feature].mean())
        print(trues[feature].mean())
        features_falses.append(falses[feature].mean())
        print(falses[feature].mean())

    ind = np.arange(len(features))
    width = 0.35
    print(ind)

    plt.bar(ind, features_trues, 0.35, label='Liked')
    plt.bar(ind + width, features_falses, 0.35, label='Disliked')

    plt.ylabel("Avg. Value")
    plt.xticks(ind + width / 2, (features))
    plt.legend(loc='best')
    plt.show()


dataset = pd.read_csv('./Data/file.csv')
print(dataset.head())

# scatter_plot_two_features(dataset, ['acousticness', 'energy'])
histo_plot_frequency(dataset, 'liked')
# bar_plot_multiple_features(dataset)

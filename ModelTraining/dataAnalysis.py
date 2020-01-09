from sklearn.metrics import recall_score, precision_score
from ModelTraining.Classifiers import ForestClassifier, SequentialClassifier, SVCClassifier
from ModelTraining.Evaluation import calculate_accuracy, calculate_recall, calculate_precision, calculate_all_metrics
from ModelTraining.Preprocessing import read_csv_to_df, undersampling_dataset, shuffle_dataset, \
    split_dataset, define_parameters
from Scripts.playlist_scrambler import get_tracks_for_playlist, get_features_for_tracks
from Visualization.ConfusionMatrix import plot_confusion_matrix
import numpy as np
import pandas as pd

df = read_csv_to_df("./Data/file.csv")
df.head()
list_of_parameters = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'tempo']
df = define_parameters(df, list_of_parameters)

undersampled_dataset = undersampling_dataset(df, 150)
shuffled_dataset = shuffle_dataset(undersampled_dataset)
dataset = split_dataset(250, shuffled_dataset)

forestcf = ForestClassifier()
forestcf.train_classifier(dataset['training_set'], dataset['training_set_label'])
predicted = forestcf.test_classifier(dataset['test_set'])

calculate_all_metrics(dataset['test_set_label'], predicted)

plot_confusion_matrix(dataset['test_set_label'], predicted, classes=['Disliked', 'Liked'])

# svg_cf = SVCClassifier()
# svg_cf.train_classifier(dataset['training_set'], dataset['training_set_label'])
# predicted = svg_cf.test_classifier(dataset['test_set'])
# calculate_all_metrics(dataset['test_set_label'], predicted)

# sequ_cf = SequentialClassifier()
# sequ_cf.train_classifier(dataset['training_set'], dataset['training_set_label'])
# predicted = sequ_cf.test_classifier(dataset['test_set'], dataset['test_set_label'])
# calculate_all_metrics(dataset['test_set_label'], predicted)

# k_neig = KNeighbours()
# k_neig.train_knei_classifier(dataset['training_set'], dataset['training_set_label'])
# predicted = k_neig.test_knei_classifier(dataset['test_set'], dataset['test_set_label'])
# calculate_all_metrics(dataset['test_set_label'], predicted)

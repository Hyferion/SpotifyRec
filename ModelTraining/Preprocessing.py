import pandas as pd


def read_csv_to_df(file):
    return pd.read_csv(file)


def define_parameters(df, list_of_parameters):
    list_of_parameters.append('liked')
    return df[list_of_parameters]


def split_dataset(trainingsize, df):
    training_set = df[:trainingsize]
    training_set_label = training_set['liked']
    training_set = training_set.drop(columns=['liked'])

    test_set = df[trainingsize:]
    test_set_label = test_set['liked']
    test_set = test_set.drop(columns=['liked'])
    return {'training_set': training_set, 'training_set_label': training_set_label, 'test_set': test_set,
            'test_set_label': test_set_label}


def shuffle_dataset(df):
    return df.sample(frac=1)


def undersampling_dataset(df, size):
    # Put all the fraud class in a separate dataset.
    underrepresented_class = df.loc[df['liked'] == False]

    # Randomly select n observations
    overrepresented_class = df.loc[df['liked'] == True].sample(n=size, random_state=42)

    # Concatenate both dataframes again
    normalized_df = pd.concat([underrepresented_class, overrepresented_class])

    return normalized_df

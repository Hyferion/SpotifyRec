import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV


def read_csv_to_df(file):
    return pd.read_csv(file)


def split_df(trainingsize, df):
    training_set = df[:trainingsize]
    training_set_label = training_set['liked']
    training_set = training_set.drop(columns=['liked'])

    test_set = df[trainingsize:]
    test_set_label = test_set['liked']
    test_set = test_set.drop(columns=['liked'])

    return {'training_set': training_set, 'training_set_label': training_set_label, 'test_set': test_set,
            'test_set_label': test_set_label}


class ForestClassifier:

    def __init__(self):
        self.forest_clf = RandomForestClassifier(random_state=42)

    def train_forest_classifier(self, training_set, training_set_label):
        self.forest_clf.fit(training_set, training_set_label)

    def test_forest_classifier(self, test_set, test_set_label):
        predicted = self.forest_clf.predict(test_set)
        print(predicted)
        acc = np.mean(predicted == test_set_label)
        print(acc)


class SGDCClassifier:

    def __init__(self):
        self.sgd_clf = SGDClassifier(max_iter=20, tol=-np.infty, random_state=42)

    def train_sgdc_classifier(self, training_set, training_set_label):
        self.sgd_clf.fit(training_set, training_set_label)

    def test_sgdc_classifier(self, test_set, test_set_label):
        predicted = self.sgd_clf.predict(test_set)
        print(predicted)
        acc = np.mean(predicted == test_set_label)
        print(acc)


df = read_csv_to_df("./file.csv")

df.head()

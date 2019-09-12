import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from tensorflow import keras
import tensorflow as tf


class BaseClassifier:

    def train_classifier(self, training_set, training_set_label):
        self.classifier.fit(training_set, training_set_label)
        print("Model trained")

    def test_classifier(self, test_set):
        predicted = self.classifier.predict(test_set)
        print(predicted)
        return predicted


class KNeighbours(BaseClassifier):
    def __init__(self):
        self.classifier = KNeighborsClassifier()


class ForestClassifier(BaseClassifier):

    def __init__(self):
        self.classifier = RandomForestClassifier(random_state=42)


class SGDCClassifier(BaseClassifier):

    def __init__(self):
        self.sgd_clf = SGDClassifier(max_iter=100, tol=-np.infty, random_state=42)


class SVCClassifier(BaseClassifier):

    def __init__(self):
        self.svc_clf = SVC(kernel="linear", C=0.025)


class SequentialClassifier():

    def __init__(self):
        self.model = tf.keras.Sequential()
        self.model.add(keras.layers.Dense(32, input_shape=(10,)))
        self.model.add(keras.layers.Dense(2, activation='softmax'))
        self.model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.01),
                           loss=tf.keras.losses.sparse_categorical_crossentropy,
                           metrics=['accuracy'])

    def train_classifier(self, training_set, training_set_label):
        self.model.fit(training_set, training_set_label, epochs=10)

    def test_classifier(self, test_set, test_set_label):
        test_loss, test_acc = self.model.evaluate(test_set, test_set_label)
        print(test_loss)
        print(test_acc)

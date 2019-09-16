import numpy as np
from sklearn.metrics import recall_score, precision_score


def calculate_all_metrics(y_test_true, predicted):
    calculate_accuracy(y_test_true, predicted)
    calculate_precision(y_test_true, predicted)
    calculate_recall(y_test_true, predicted)


def calculate_accuracy(y_test_true, predicted):
    accuracy = np.mean(predicted == y_test_true)
    print("Accuracy: " + str(accuracy))
    return accuracy


def calculate_recall(y_test_true, predicted):
    recall = recall_score(y_test_true, predicted)
    print("Recall: " + str(recall))
    return recall


def calculate_precision(y_test_true, predicted):
    precision = precision_score(y_test_true, predicted)
    print("Precision: " + str(precision))
    return precision

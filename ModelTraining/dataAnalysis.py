from sklearn.metrics import recall_score, precision_score
from ModelTraining.Classifiers import ForestClassifier, SequentialClassifier
from ModelTraining.Preprocessing import read_csv_to_df, undersampling_dataset, shuffle_dataset, \
    split_dataset, define_parameters
from Visualization.ConfusionMatrix import plot_confusion_matrix
import numpy as np

df = read_csv_to_df("./Data/file.csv")
df.head()

df = define_parameters(df, ['acousticness', 'danceability', 'energy', 'instrumentalness', 'tempo'])

undersampled_dataset = undersampling_dataset(df, 150)
shuffled_dataset = shuffle_dataset(undersampled_dataset)
dataset = split_dataset(120, shuffled_dataset)

forestcf = ForestClassifier()
forestcf.train_classifier(dataset['training_set'], dataset['training_set_label'])
predicted = forestcf.test_classifier(dataset['test_set'])

accuracy = np.mean(predicted == dataset['test_set_label'])
print("Accuracy: " + str(accuracy))

recall_score = recall_score(dataset['test_set_label'], predicted)
print("Recall: " + str(recall_score))
precision_score = precision_score(dataset['test_set_label'], predicted)
print("Precision: " + str(precision_score))

sequ_cf = SequentialClassifier()
sequ_cf.train_classifier(dataset['training_set'], dataset['training_set_label'])
sequ_cf.test_classifier(dataset['test_set'], dataset['test_set_label'])

# plot_confusion_matrix(dataset['test_set_label'], predicted, classes=['Disliked', 'Liked'])
# k_neig = KNeighbours()
# k_neig.train_knei_classifier(dataset['training_set'], dataset['training_set_label'])
# k_neig.test_knei_classifier(dataset['test_set'], dataset['test_set_label'])

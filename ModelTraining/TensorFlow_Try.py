from tensorflow import keras
from ModelTraining.dataAnalysis import read_csv_to_df
import tensorflow as tf
import numpy as np

print(tf.version.VERSION)
print(tf.keras.__version__)

df = read_csv_to_df("./Data/file.csv")
sets = split_df(54, df)
training_set = sets['training_set']
print(training_set.shape)
training_set_label = sets['training_set_label']
print(training_set_label)
test_set = sets['test_set']
print(test_set)
test_set_label = sets['test_set_label']
print(test_set_label)

model = tf.keras.Sequential()
model.add(keras.layers.Dense(32, input_shape=(10,)))
model.add(keras.layers.Dense(2, activation='softmax'))
model.compile(optimizer=tf.compat.v1.train.RMSPropOptimizer(0.01), loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])
model.fit(training_set, training_set_label, epochs=10)
test_loss, test_acc = model.evaluate(test_set, test_set_label)

print('\nTest accuracy:', test_acc)

predictions = model.predict(test_set)

print(predictions)
print(np.argmax(predictions[0]))
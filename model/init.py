import tensorflow as tf
import csv
import numpy as np
from tensorflow import keras

features = []
labels = []
with open('daily.csv', newline='\n') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)
    for row in reader:
        date = row[0].split("-")
        features.append(date)
        labels.append(row[1])


model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')


xs = np.array(features)
ys = np.array(labels, dtype=float)

model.fit(xs, ys, epochs=500)

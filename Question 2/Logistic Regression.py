import numpy as np # linear algebra
import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense,
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

tbCallBack = keras.callbacks.TensorBoard(log_dir='\Graph', histogram_freq=0)

data = pd.read_csv("heart.csv", header=0)
X = data.values[:, 0:13]
y = data.values[:, 13]

train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.25, random_state=0)

model = Sequential()
model.add(Dense(32, input_shape=(13,), activation='softmax'))
model.add(Dense(1, activation='softmax'))
model.compile(loss='binary_crossentropy', metrics=['accuracy'], optimizer='SGD')

# Actual modelling
history = model.fit(train_X, train_y, validation_data=(test_X, test_y), verbose=0, epochs=100, batch_size=2, callbacks=[tbCallBack])

evaluation = model.evaluate(test_X, test_y, verbose=1)
print('Loss : %.2f, Accuracy: %.2f' % (evaluation[0], evaluation[1]))

plt.plot(history.history['val_loss'])
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
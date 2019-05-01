import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.layers import Dropout
from keras.optimizers import Adam, SGD
import matplotlib.pyplot as plt

# load dataset
dataset = pd.read_csv("esp_studies1.csv", header=0, encoding = "ISO-8859-1")
print(dataset.columns)
print(dataset.head())

print(dataset.info)

#Predicting if user has ESP in the final
cols = ['Group', 'Rouder1', 'Year', 'numtrials', 'numhits', 'k', 'pi_0', 'pi_hat', 'Z_obs', 'eff_sz1', 'eff_sz2']
x = dataset[cols]
y = dataset['InFinal']
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.25, random_state=0)

tbCallBack = keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=0,
write_graph=True, write_images=True)
n_cols = x.shape[1]

lrate = 0.01

model = Sequential() # create model
model.add(Dense(32, input_dim=n_cols, init='uniform', activation='sigmoid'))
model.add(Dense(64, activation="relu", kernel_initializer="uniform"))
model.add(Dense(64, activation="relu", kernel_initializer="uniform"))
model.add(Dense(64, activation="relu", kernel_initializer="uniform"))
model.add(Dense(32, activation="relu", kernel_initializer="uniform"))
model.add(Dense(1, activation='tanh')) # output layer
model.add(Dropout(0.1))
#Using Adam Optimizer Learning rate = .01
model.compile(optimizer=Adam(lr=.001),loss='mean_squared_error', metrics=['accuracy'])

history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=50, batch_size=32, callbacks=[tbCallBack])
scores = model.evaluate(X_test, Y_test, verbose=0)

train_score = model.evaluate(X_train, Y_train, verbose=0)
valid_score = model.evaluate(X_test, Y_test, verbose=0)

print('Trained: ', round(train_score[1], 4), ', trained data loss', round(train_score[0], 4))
print('Validation: ', round(valid_score[1], 4), ', validation loss ', round(valid_score[0], 4))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
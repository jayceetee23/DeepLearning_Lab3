
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
import re
from sklearn.preprocessing import LabelEncoder
from keras.utils.np_utils import to_categorical
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np # linear algebra

data = pd.read_csv('train.csv')
#Keeping only the neccessary columns
data = data[['Phrase', 'Sentiment']]

data['Phrase'] = data['Phrase'].apply(lambda x: x.lower())
data['Phrase'] = data['Phrase'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))

print(data[data['Sentiment'] == 0].size)
print(data[data['Sentiment'] == 1].size)
print(data[data['Sentiment'] == 2].size)
print(data[data['Sentiment'] == 3].size)
print(data[data['Sentiment'] == 4].size)

max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')

tokenizer.fit_on_texts(data['Phrase'].values)
print(data['Phrase'].values)
X = tokenizer.texts_to_sequences(data['Phrase'].values)
print(X)
X = pad_sequences(X)
print(X)
X = np.expand_dims(X, axis=2)

labelencoder = LabelEncoder()
integer_encoded = labelencoder.fit_transform(data['Sentiment'])
y = to_categorical(integer_encoded)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# print(X_train.shape, Y_train.shape)
# print(X_test.shape, Y_test.shape)
batch_size = 32
num_classes = Y_test.shape[1]
# Create the model
model = Sequential()
model.add(Conv1D(32,5,input_shape=(45,1), padding='same', activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Conv1D(128,5, activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(MaxPooling1D(pool_size=5))

model.add(Flatten())
model.add(Dense(64, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
# Compile model
epochs = 2
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
print(model.summary())
# Fit the model
model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=epochs, batch_size=64)
# Final evaluation of the model
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))



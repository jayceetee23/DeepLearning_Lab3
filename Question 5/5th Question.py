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
#data2 = pd.read_csv('test.csv')
#Keeping only the neccessary columns
data = data[['Phrase', 'Sentiment']]

data['Phrase'] = data['Phrase'].apply(lambda x: x.lower())
data['Phrase'] = data['Phrase'].apply((lambda x: re.sub('[^a-zA-z0-9\s]', '', x)))

print(data[data['Sentiment'] == 0].size)
# print(data[data['Sentiment'] == '1'].size)
# print(data[data['Sentiment'] == '2'].size)
# print(data[data['Sentiment'] == '3'].size)
# print(data[data['Sentiment'] == '4'].size)

# for idx, row in data.iterrows():
#     row[0] = row[0].replace('rt', ' ')

max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')

tokenizer.fit_on_texts(data['Phrase'].values)
print(data['Phrase'].values)
X = tokenizer.texts_to_sequences(data['Phrase'].values)
print(X)
X = pad_sequences(X)
print(X)

embed_dim = 128
lstm_out = 196
def createmodel():
    model = Sequential()
    model.add(Embedding(max_features, embed_dim, input_length=X.shape[1]))
    model.add(SpatialDropout1D(0.4))
    model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(5, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
# print(model.summary())

labelencoder = LabelEncoder()  #Do not need bc sentiments are already numeric
integer_encoded = labelencoder.fit_transform(data['Sentiment'])
y = to_categorical(integer_encoded)
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.33, random_state=42)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

batch_size = 32
model = createmodel()
model.fit(X_train, Y_train, epochs=2, batch_size=batch_size, verbose=5)
score, acc = model.evaluate(X_test, Y_test, verbose=5, batch_size=batch_size)
print(score)
print(acc)

#model.save('model.h5')

# model = KerasClassifier(build_fn = createmodel,verbose=0)
# batch_size = [10, 20]
# epochs = [1, 2]
# param_grid = dict(batch_size=batch_size, epochs=epochs)
#
# from sklearn.model_selection import GridSearchCV
#
# grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=1)
# grid_result = grid.fit(X_train, Y_train)
# # summarize results
# print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
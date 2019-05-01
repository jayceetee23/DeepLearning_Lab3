# Question 3 Lab 3 (CNN on Kaggle Dataset)

# Import Necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Activation
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

import os # used for directory operations
import cv2


data_dir = 'C:/Users/Shanoa/Desktop/data/natural_images'
CATEGORIES = ['airplane', 'car', 'cat', 'dog', 'flower', 'fruit', 'motorbike', 'person']

airplane = os.listdir(data_dir)

for category in CATEGORIES:
    path = os.path.join(data_dir, category) # path to img dir
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE) # converted image to grayscale

# print(img_array)

# convert all to same image size 32x32
img_size = 32
new_array = cv2.resize(img_array, (img_size,img_size))


training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(data_dir, category)  # path to img dir
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)  # converted image to grayscale
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_num])
            except Exception as e: # pass deviant images
                pass

create_training_data()

print(len(training_data))


# Shuffle data
import random
random.shuffle(training_data)

# for sample in training_data[:10]:
#     print(sample[1])

x = [] # Feature Set
y = [] # Label Set

for features, label in training_data:
    x.append(features)
    y.append(label)

x = np.array(x).reshape(-1, img_size, img_size, 1) # one for grayscale, can do 3 for at the end for color

# normalize inputs from 0-255 to 0.0-1.0

x = np.array(x).astype('float32')
x = x / 255.0

# 8 classes in dataset
num_classes = 8

# Create the model
model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=x.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) #maybe use adam optimizer?

model.fit(x,y, batch_size=32, epochs=5, validation_split=0.1)


# DeepLearning_Lab3

## I. Introduction

The purpose of this programming lab is to demonstrate the use and creation of different kinds of neural network models. These models are created from different datasets and can be used to make predictions on new sets of data.
 
 ## II. Objectives.
 
Provided were 6 questions that would allow one to understand the different neural network models in different situations. In the following examples we will be working with .csv datasets as well as image datasets. The questions are as follows:
 
![Questions](https://user-images.githubusercontent.com/47049525/57011101-9c81ea80-6bc5-11e9-840c-3052bfc2c8ad.PNG)

## III. Approaches/Methods / IV. Workflow
## 1.

Code:
![Q1 Code](https://user-images.githubusercontent.com/47049525/57013267-4a929200-6bd0-11e9-825a-330f01f31278.PNG)
![Q1 Code 2](https://user-images.githubusercontent.com/47049525/57013268-4a929200-6bd0-11e9-8b47-a9848616a808.PNG)

Part a:

![Loss Plot Q1](https://user-images.githubusercontent.com/47049525/57013141-b6c0c600-6bcf-11e9-99a2-07990aac821a.png)
![TensorBoard Q1](https://user-images.githubusercontent.com/47049525/57013143-b7595c80-6bcf-11e9-9761-a4310200a01b.png)

Part b:
[part b.txt](https://github.com/jayceetee23/DeepLearning_Lab3/files/3134225/part.b.txt)

## 2.
This question implements Logistic Regression on the heart disease uci dataset.
![Question 2 Code](https://user-images.githubusercontent.com/47049525/57012644-313c1680-6bcd-11e9-9f6d-ee8fa2b4cfb7.PNG)

Q2 Loss:
![Q2 loss](https://user-images.githubusercontent.com/47049525/57013118-91cc5300-6bcf-11e9-93b6-45e32c5ec3c8.png)


## 3.
This question implements the image classification with CNN (Convolutional Neural Network) on the natural-images dataset.

Code:
![Code1](https://user-images.githubusercontent.com/47049525/57012540-ae1ac080-6bcc-11e9-9556-2534ef210031.PNG)
![Code2](https://user-images.githubusercontent.com/47049525/57012542-ae1ac080-6bcc-11e9-8218-8a9e82be1da8.PNG)

Results:
![Question 3 CNN Result](https://user-images.githubusercontent.com/47049525/57012110-80347c80-6bca-11e9-90c0-17e365f10164.PNG)


## 4.
This question implements the text classification with CNN (Convolutional Neural Network) on the following movie reviews dataset.

Code:
![CNN_1st](https://user-images.githubusercontent.com/47049525/57012094-609d5400-6bca-11e9-8f75-bf3b9456f0f9.PNG)
![CNN_2nd](https://user-images.githubusercontent.com/47049525/57012095-609d5400-6bca-11e9-97af-0731240d04b4.PNG)

Output:
![CNN_Output_1](https://user-images.githubusercontent.com/47049525/57012096-609d5400-6bca-11e9-89d2-6e827085e607.PNG)
![CNN_Output_2](https://user-images.githubusercontent.com/47049525/57012097-6135ea80-6bca-11e9-84fe-2d0ed275f1e6.PNG)


## 5.

This question implements the text classification with LSTM (Long Short Term Memory) on the following movie reviews dataset.

Code:
![5th Question Code Part 1](https://user-images.githubusercontent.com/47049525/57012046-292ea780-6bca-11e9-9a41-4d8e6a5f64aa.PNG)
![5th Question Code Part 2](https://user-images.githubusercontent.com/47049525/57012047-292ea780-6bca-11e9-85ba-d1c3bccf8001.PNG)

Output:
![5h Question Output](https://user-images.githubusercontent.com/47049525/57012048-292ea780-6bca-11e9-8748-d65e3ee739c6.PNG)


## 6.
Using LSTM model, we got 62% accuracy over 50.48% with CNN model. Thus, for this case, LSTM is clearly a better way to go.

Holding other Hyperparameters constant:

1-When added more layers to CNN, accuracy increased from 50.48% to 50.55%.

2-When changed the Epoch from 2 to 5 in CNN model, accuracy increased from 50.48% to 50.81%.

3-When used “Sigmoid” instead of “Relu” in CNN model, accuracy remained unchanged at 50.48%.

4-When used “Tanh” instead of “Relu” in CNN model, accuracy increased from 50.48% to 50.91%.

5-When changed learning rate from 0.01 to 0.02 in CNN model, accuracy increased from 50.48% to 50.82%.

Changed Layer Number:
![CNN_Changed_Layer_Num](https://user-images.githubusercontent.com/47049525/57011637-46627680-6bc8-11e9-9c2a-de231ef18ee0.PNG)

Changed Epoch from 2 to 5:
![CNN_5Epochs](https://user-images.githubusercontent.com/47049525/57011576-f4215580-6bc7-11e9-82f6-64b92fc51116.PNG)

Used Sigmoid Function:
![CNN_Sigmoid](https://user-images.githubusercontent.com/47049525/57011639-46fb0d00-6bc8-11e9-91c7-f034e8f34c9f.PNG)

Used Tanh Function:
![CNN_Tanh](https://user-images.githubusercontent.com/47049525/57011635-46627680-6bc8-11e9-8caf-f308e69c0b98.PNG)

Changed Learning rate from 0.01-0.02:
![CNN_L_Rate_0 02](https://user-images.githubusercontent.com/47049525/57011638-46627680-6bc8-11e9-9f2a-8e684166fa44.PNG)


## V. Dataset

Datasets used:
Question 1: esp_studies1
Question 2: https://www.kaggle.com/ronitf/heart-disease-uci
Question 3: https://www.kaggle.com/prasunroy/natural-images
Questions 4-6: https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data.

## VI. Parameters

-Questions 1 and 2 use keras to implement Linear Regression and Logistic Regression, respectively.
-Question 3 uses CNN on the natural images dataset.
-Questions 4-6 use CNN, LSTM models and compares which of the two give the best result.

## VII Evaluation and Discussion

Questions provided allowed for practical implementation and understanding of DeepLearning and various neural network models. Each example provides different use cases from image classification to reading .csv datasets. 

## VIII Conclusion

In conclusion, this lab exercise provided good demonstrations to an introduction to DeepLearning and different neural networks. These types of examples can be extremely useful in real world applications, from image recognition software to creating models to make predictions on various datasets.

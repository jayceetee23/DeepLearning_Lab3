# DeepLearning_Lab3

## I. Introduction

The purpose of this programming lab is to demonstrate the use and creation of different kinds of neural network models. These models are created from different datasets and can be used to make predictions on new sets of data.
 
 ## II. Objectives.
 
Provided were 6 questions that would allow one to understand the different neural network models in different situations. In the following examples we will be working with .csv datasets as well as image datasets. The questions are as follows:
 
![Questions](https://user-images.githubusercontent.com/47049525/57011101-9c81ea80-6bc5-11e9-840c-3052bfc2c8ad.PNG)

## III. Approaches/Methods / IV. Workflow
## 1.
To solve question one, a class was used so that input could be obtained without any overlapping accounts getting in the way.

![Screenshot](https://i.imgur.com/vYuqCZ3.png)

Since input is obtained in one line, the program will split the Command, and money amount and choose which option to pick based on the length of the list. Any input not recognized will throw an invalid input message at the user but is case insensitive.

![Screenshot](https://i.imgur.com/3F7ozmb.png)

## 2.
Iterating through the tuplet list and checking if the key existes within the dictionary before appending the value to the to a new list.. Since keys cannot have multiple values, an appended list was the alternative to create a "Mutli valued Key".

![Screenshot](https://i.imgur.com/CACWZND.png)

![Screenshot](https://i.imgur.com/WPYiGd2.png)

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

The only dataset used was the data table about the United States of America and its respective states.
![Screenshot](https://i.imgur.com/To2WFXe.png)

## VI. Parameters

There were no parameters as these were indivudual questions with no correlation to eachother.

## VII Evaluation and Discussion

The questions provided were quite challenging. Additional features could have been added to many of the programs above such as error handling, or bad input. Some of the questions were confusing to implement as the questions could have been clarified more. Such as in question 6 whether it was asking for the entire table or just the States and Capital. Question 5 did not have a clear goal in output other than just to implement classes.

## VIII Conclusion

Overall this lab was an excellent exercise to prepare for Deep Learning using python. It has gone over the basics of scraping the web, and using its basic functions. 

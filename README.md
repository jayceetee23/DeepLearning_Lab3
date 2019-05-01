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
To find if students shared or had unique classes from each other, first add them into seperate lists of "Python class" and "Web Application.

![Screenshot](https://i.imgur.com/e6AyBzi.png)

Once the lists are obtained, create two new lists for common classes and unique classes. Iterating through a for loop to check if Python[x] is in WebApplication[x]. If the element is found in the comparison lists, they share a school class and are appended to "both_list". The reverse is done for the "not_common_list". Iterate through both lists of Python and Webapplication and check if they are "not in" each others elements. If so, append to "not_common_list".

![Screenshot](https://i.imgur.com/W5fFIsf.png)

## 4.
The user will input a string and it will be checked for duplicate characters and longest substring.

![Screenshot](https://i.imgur.com/sgTPPzB.png)

Once the input is recieved it is iterated through a loop. Once in the loop if a unique character is not in an empty list made outside of the loop, it is appended to the list and a temporary value is increased, this is how unique character count is tracked. If its already in the list reset, the length. After iterating compare the final answer to the temporary answer and temporary length to the final legnth to find which is bigger to output.

![Screenshot](https://i.imgur.com/x0n3mnr.png)

## 5.

<details><summary>Question 5 Code</summary>
<p>
  
```
import random

print("\n")
print("Airline Booking System\n")


class Person:   # base class #1 Person ==> Passenger and Employee Class will inherit from Person

    def __init__(self, first, last):    # example of use of self.
        self.first = first
        self.last = last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


class Passenger(Person):    # class #2 Passenger. Inherits from Person class

    def __init__(self, first, last, passport, choice):
        super().__init__(first, last)   # super call
        self.passport = passport
        self.choice = choice


class Employee(Person): # class #3 Employee. Inherits from Person class

    def __init__(self, first, last, job_title):
        super().__init__(first, last)   # super call
        self.job_title = job_title


class Destination: # class #4 base class; used for displaying flight options
    def __init__(self, location):
        self.location = location

    def display_location(self):
        print("List of current available flights:")
        print("-----------------------------------")
        for flights in self.location:
            print(flights)


class Airline: # class #5 base class; generates random number for flight and gate number
    def __init__(self, flight_number = random.randint(100,700), gate_number = random.randint(1,40)):
        self.flight_number = flight_number
        self.gate_number = gate_number

    def plane_info(self):
        print("Flight number:", self.flight_number, "Gate number:", self.gate_number)


class Payment(Passenger): # class #6, example of multiple inheritance, inherits from Passenger that inherits from Person
    def __init__(self, first, last, passport, choice, card):
        super().__init__(first, last, passport, choice)
        self.__card = card  # private data member


def main():


    flights = Destination([("Select 1:", "NRT", 1800), ("Select 2:", "LAX", 550), ("Select 3:", "MCI", 300)])
    # instance of Destination; class will display different flight options

    plane1 = Airline() # instance of Airline, will RNG flight number and gate number for plane


    done = False    # allows for users who choose option one to be able to opt into option 2

    while done is False:

        print("\n")
        print("Options Menu")
        print("1: Display available flights")
        print("2: Book a flight")

        option = int(input("Select option: "))

        if option == 1:
            print("\n")
            flights.display_location()  # display flight options

        if option == 2:

            booking_choice = int(input("To book as a passenger, enter 1. to book as an employee, enter 2. "))
            # book as a passenger or employee

            if booking_choice == 1:

                # instance of Passenger; user inputs needed information for class
                per1 = Passenger(input("First name: "), input("Last name: "), input("Passport information: "),
                                 int(input("Flight Choice: ")))

                if per1.choice == 1:

                    # instance of Payment; overrides per1 and allows to enter credit card information
                    per1 = Payment(per1.first, per1.last, per1.passport, per1.choice,
                                   int(input("Enter Card Information:")))

                    print("PRINTING TICKET:\n")
                    print(per1.fullname())
                    plane1.plane_info()
                    print("Flight Destination: NRT. Total Cost = $1800.00")
                    input()
                    done = True

                elif per1.choice == 2:

                    # instance of Payment; overrides per1 and allows to enter credit card information
                    per1 = Payment(per1.first, per1.last, per1.passport, per1.choice,
                                   int(input("Enter Card Information: ")))

                    print("PRINTING TICKET:\n")
                    print(per1.fullname())
                    plane1.plane_info()
                    print("Flight Destination: LAX. Total Cost = $550.00")
                    input()
                    done = True

                elif per1.choice == 3:

                    # instance of Payment; overrides per1 and allows to enter credit card information
                    per1 = Payment(per1.first, per1.last, per1.passport, per1.choice,
                                   int(input("Enter Card Information: ")))

                    print("PRINTING TICKET:\n")
                    print(per1.fullname())
                    plane1.plane_info()
                    print("Flight Destination: MCI. Total Cost = $300.00")
                    input()
                    done = True

            elif booking_choice == 2:

                # instance of Employee class, user enters first/last name and job title
                employee = Employee(input("First name: "), input("Last name: "), input("Enter job title: "))
                print(employee.fullname())
                print(employee.job_title)
                print("Thank you for signing in. Please wait for job assignment.")
                input()
                done = True
```
</p>
</details>


Before using the code, you must import random to create a random integer for the ticket number. 6 Classes were created with Person being the main class. Employee and Passanger are derived from these. Destination and Airline are base classes independant from each other, and payment is derived from Passenger since they will be the only users to pay credit.

![Screenshot](https://i.imgur.com/PKnhOhS.png)

Depending on which person is choosing, the program directs them towards a payment or to be stationed for their job.

![Screenshot](https://i.imgur.com/Bnotd6B.png)

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

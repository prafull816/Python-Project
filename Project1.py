# Guess the Number

"""
Setep1 : In this code code will chose the one random number 

Setp2 : In this step player can choose the random number 

Setp3 : in this step program will tell to player his enter no is write or wrong 

____ this steps are continue till user enter the corrct input _____
"""

import random
 

target = random.randint(1,100)

while True:
    userChoice = int(input("Guess the target  Or Quite (Q) : "))
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!!")
        break
    elif(userChoice < target):

        print("Your number was too sma60ll. Take a bigger guess...")

    else:
        print("Yor number was too big. Take a smaller guess...")


print("---------GAME OVER---------")



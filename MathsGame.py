#import random function and the reduce function
import random
from random import randint
from functools import reduce

#initialise global variables for the all the functions to reference
level = 1
answeredCorrect = 0
answeredIncorrect = 0
ransum = False

#the addition function, generates two random numbers, validates the input and verifies the answer
#will recursively call itself it the user wants to continue and random is off
def addition():
    num1 = randint(1, (level+3))
    num2 = randint(1, (level+3)) 
    print("What is ", num1, "+", num2, " ?")
    
    if validatedInput() == num1+num2:
        correct()
    else:
        incorrect(num1+num2)

    if ransum == False:
        if (contQuest()):
            addition()

#the subtraction function
#same structure as the addition function but the second number generated is always <= the first number to ensure the answer isn't negative     
def subtraction():
    num1 = randint(1, (level+3))
    num2 = randint(1, num1)
    print("What is ", num1, "-", num2, " ?")
    
    if validatedInput() == num1-num2:
        correct()
    else:
        incorrect(num1-num2)

    if ransum == False:
        if (contQuest()):
            subtraction()

#the multiplicate function
#same structure as the addition function
def multiplication():
    num1 = randint(1, (level+3))
    num2 = randint(1, (level+3))
    print("What is ", num1, "X", num2, " ?")
    
    if validatedInput() == num1*num2:
        correct()
    else:
        incorrect(num1*num2)

    if ransum == False:
        if (contQuest()):
            multiplication()

#the division function
#same structure as the addtion function but the second number generated can only be a factor of the first number to esnure the answer isn't fractional
def division():
    num1 = randint(1, (level+3))
    num2 = random.choice(list(factors(num1)))
    print("What is ", num1, "÷", num2, " ?")
    
    if validatedInput() == num1/num2:
        correct()
    else:
        incorrect(num1/num2)

    if ransum == False:
        if (contQuest()):
            division()

#function to return a list of the factors of a given number
def factors(n):    
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#the random sum function
#turns the random variable to on so the function dont recursivly call themselves and negate the randomness
#randomly chooses from the list of the 4 different function and calls them, turns random variable to off if the user is finished
def randomSums():
    global ransum
    ransum = True
    random.choice([addition, subtraction, multiplication, division])()
    if (contQuest()):
            randomSums()
    else:
        ransum = False

#if the answer is correct, it will increment a variable and reset the 'incorrect' variable to 0
#if 3 are right in a row, the level is increased by 1 to a maximum of 7
def correct():
    print("You answered correctly")
    global answeredCorrect
    global answeredIncorrect
    global level
    answeredIncorrect = 0
    answeredCorrect += 1
    if (answeredCorrect) == 3 and (level < 7):
        answeredCorrect = 0
        level += 1
        print("These questions are too easy for you, I've moved you to level: ", level)

#if the answer is incorrect, it will increment a variable and reset the 'correct' variable to 0
#if 3 are wrong in a row, the level is decreased by 1 to a minimum of 1
#the correctanswer is taken as a parameter and printed to inform the user
def incorrect(correctAnswer):
    print("You answered incorrectly, the correct answer is ", correctAnswer)
    global answeredCorrect
    global answeredIncorrect
    global level
    answeredCorrect = 0
    answeredIncorrect += 1
    if (answeredIncorrect == 3) and (level > 1):
        answeredIncorrect = 0
        level -= 1
        print("You seem to be struggling with these questions, I've moved you down to level: ", level)

#function that asks if the user wants to continue the same line of questions, if yes return true and false if no
def contQuest():
    global answeredCorrect
    global answeredIncorrect
    global level
    while True:
            i = input("Press Y to try another sum or N to stop.\n")
            if i == "Y" or i == "y":
                return True
            elif i == "N" or  i == "n":
                answeredCorrect = 0
                answeredIncorrect = 0
                level = 1
                return False

#funtion that gets the user input and checks if it is a number, if not it informs the user it wants a number
def validatedInput():
    answer = input()
    try:
        answer = int(answer)
    except ValueError:
        print("Please enter a number")
    return answer

#creates a dictionary of the 5 functions and 1 function to exit
option = None
menu = {1:addition, 2:subtraction, 3:multiplication, 4:division, 5:randomSums, 6:exit}

#if the option is not exit is will print the menu and wait for the user to select an option, if the user doesn't select one of the 6 options it asks again
while option != 6:
        print("1:addition\n2:subtraction\n3:multiplication\n4:division\n5:randomSums\n6:exit")
        option = int(input("Please select an option\n"))
        if option >= 1 and option <= 5:
            menu[option]()

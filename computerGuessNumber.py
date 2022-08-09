import random
from re import L


def guessTheNumberComputer(x):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("  Welcome to guess the number: Computer Version  ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Select a number between 1 and {x} for the computer to try to guess")

    inferiorLimit = 1
    superiorLimit = x

    answer = ""
    while answer != "t":
        # Generate Prediction
        if superiorLimit != inferiorLimit:
            prediction = random.randint(inferiorLimit,superiorLimit)
        else:
            prediction = inferiorLimit # or superiorLimit (are the same)

        # Get an user answer
        answer = input(f"My prediction is {prediction}, if its bigger, enter (b). If its lower, enter (l). If its true, enter (t): ".lower())

        if answer == "b":
            superiorLimit = prediction - 1
        elif answer == "l":
            inferiorLimit = prediction + 1
    
    print(f"Awesome! The computer guessed the number correctly: {prediction}")


guessTheNumberComputer(10)
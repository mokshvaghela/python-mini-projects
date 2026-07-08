# PROJECT 1:
# Stone, Paper, Scissors Game

'''
Here we take values like:
Stone = -1
Paper = 0
Scissors = 1
'''

import random

dict = {"Stone" : -1, "Paper" : 0, "Scissors" : 1}
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
you = dict[youstr]
reverseDict = { -1 : "Stone", 0 : "Paper", 1 : "Scissors"}
print(f"You choose {reverseDict[you]} \n Computer choose {reverseDict[computer]}")

if (computer==you):
    print("Its a draw!")

else:
    if (computer == -1 and you == 1):
        print("You Lose!")
    elif (computer == -1 and you == 0):
        print("You Win!")
    elif (computer == 1 and you == 0):
        print("You Lose!")
    elif (computer == 1 and you == -1):
        print("You Win")
    elif (computer == 0 and you == -1):
        print("You Lose!")
    elif (computer == 0 and you == 1):
        print("You Win!")
    else:
        print("Something went wrong!")
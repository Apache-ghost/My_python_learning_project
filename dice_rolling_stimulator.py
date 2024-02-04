import random
def roll_dice():
    roll=input("Do you want to roll?yes or no: ")
    while roll.lower()=="Yes".lower():
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"dice roll: {dice1} and {dice2}")
        roll=input("Do you want to roll again?yes or no: ")
roll_dice()
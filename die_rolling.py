import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll

while True: 
    players=input("Enter the number of player(2-4): ")
    if players.isdigit():
        players=int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Enter a number btw (2-4): ")
    else:
        print("invalid try again ! ")

max_score=50
players_score=[0 for _ in range(len(players))]

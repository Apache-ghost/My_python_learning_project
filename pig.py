import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (between 2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2-4.")
    else:
        print("Please enter a valid number.")

max_score = 50
players_scores = [0] * players

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started.")
        print("Your total score is:", players_scores[player_idx])
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your current score is:", current_score)
                players_scores[player_idx] += current_score
                print("The total score is:", players_scores[player_idx])

                max_score = max(players_scores)
                winning_idx = players_scores.index(max_score)

                if max_score >= max_score:
                    print("Player number", winning_idx + 1, "is the winner with a max score of", max_score)
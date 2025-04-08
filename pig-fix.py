import random

def roll():
    dice_num = rand.randint(1,6)
    return dice_num

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("Let's play!")
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Enter a valid digit next time!")

max_score = 50
player_scores = [0 for _ in range(players)]

# Main game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started.")
        current_score = 0
        
        while True:
            play = input("Do you want to roll the dice? (y/n): ").strip().lower()
            if play != "y":
                break  # Player chooses to stop rolling
            
            value = roll()
            print(f"You rolled: {value}")

            if value == 1:
                print("Oops! You rolled a 1. Your turn is over, and you lose all points this round.")
                current_score = 0
                break  # End turn

            current_score += value
            print(f"Current round score: {current_score}")
        
        player_scores[player_idx] += current_score
        print(f"Total score for Player {player_idx + 1}: {player_scores[player_idx]}")

        if player_scores[player_idx] >= max_score:
            print(f"\n🎉 Player {player_idx + 1} wins with a score of {player_scores[player_idx]}! 🎉")
            exit()

import random

      

def roll():
    max_roll = 6
    min_roll = 1
    
    dice = random.randint(min_roll,max_roll)
    print(dice)
    
while True:
    players = input("Enter the number of players(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Lets play!")
    else:
        print("Enter a digit a next time foo!! ")
        break
        
max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("Player", player_idx + 1,"turn has just started")
        current_score = 0
            
while True:
    play = input("Do you want to roll the dice? (y/n): ")
    if play.lower != "y":
        break
    else:
         value = roll()
         print("You have rolled: ", value)
         current_score += value
                
                
    player_scores[player_idx] += current_score
    print("Your total score is: ", player_scores[player_idx])
            
        
    
        
        
       
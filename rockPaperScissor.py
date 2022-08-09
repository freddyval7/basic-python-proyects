import random


def play():
    user = input("Choose an option: 'ro' for rock, 'pa' for paper, and 'sc' for scissor.\n").lower()
    computer = random.choice(["ro","pa","sc"])
    
    if user == computer:
        return "Draw!"
        
    if playerWins(user, computer):
        return "You Win!"

    return "You lose!" 




def playerWins(player, opponent):
    # Return True if player wins.
    # Rock wins against Scissor (ro > sc).
    # Scissor wins against Paper (sc > pa).
    # Paper wins against Rock (pa > ro).

    if ((player == "ro" and opponent == "sc")
        or (player == "sc" and opponent == "pa")
        or (player == "pa" and opponent == "ro")):
        return True
    else:
        return False

print(play())



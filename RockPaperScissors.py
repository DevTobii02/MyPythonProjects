import random
def play():
    userinput = input("What's Your Choice ? ('r' for Rock, 's' for Scissors, 'p' for Paper) : ")
    computer = random.choice(['r', 'p', 's'])
    
    if userinput == computer:
        return "Tie"
    
    if IsWin(userinput, computer):
        return "You Win!!!"
    return "You Lost!"

def IsWin(Player, Opponent):
    if (Player == 'r' and Opponent == 's') or (Player == 's' and Opponent == 'p') or (Player == 'p' and Opponent == 'r'):
        return True
print(play())    
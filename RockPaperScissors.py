import random 
#GameVariables = ("Rock", "Paper", "Sciccors") 
UserInput = input("What's Your Choice ?  ('r' for Rock, 'p' for Paper, 's' for Scissors) : ") 
Computer = random.choice(['r', 'p', 's'])
if UserInput == Computer:
    print("It's A Tie")
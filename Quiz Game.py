Questions = ("(1). Who Is The Current President Of Nigeria ?:", 
             "(2). Who Is The Current Governer Of Lagos State ? :", 
             "(3). How Many Planets Do We Have In Our Solar System ? :", 
             "(4). How Many States Do We Have In Nigeria ? :", 
             "(5). Which Planet From The Solar System Do We Live In ? :", 
             "(6). What Is The Most Abundant Gas In Earth's Atmosphere ? :",
             "(7). Which Planet From The Solar System Is The Hottest ? : ") 

Options = (("A. Bola Ahmed Tinubu", "B. Babatunde Raji Fashola", "C. Goodluck Ebele Jonathan", "D. Peter Obi"), 
           ("A. Mobolaji Anthony", "B. Lateef Jakande", "C. Akinwunmi Ambode", "D. Babajide Olushola Sanwo-Olu"), 
           ("A. 7", "B. 9", "C. 8", "D. 5"),
           ("A. 20", "B. 38", "C. 37", "D. 36"), 
           ("A. Ires", "B. Neptune", "C. Earth", "D. Saturn"),
           ("A. Chlorine", "B. Neon", "C. Oxygen", "D. Nitrogen"),
           ("A. Pluto", "B. Saturn", "C. Jupiter", "D. Mecury"))  

CorrectAnswers = ("A", "D", "C", "D", "C", "D", "D")
Guesses = []
Score = 0 

QuestionNumber = 0  

for Question in Questions:
    print(Question) 
    for Option in Options[QuestionNumber]:
        print(Option) 
    Guess = input("Enter From The Range Of Option (A, B, C, D): ").upper()  
    Guesses.append(Guess)
    if Guess == CorrectAnswers[QuestionNumber]:
        Score += 1
        print("Correct") 
        print(Score)
    else:
        print("Incorrect Answer")
        print(f"The Correct Answer is : {CorrectAnswers[QuestionNumber]}")
    QuestionNumber +=1    
print(f"Your Total Score Is :  {Score} ")    
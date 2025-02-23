#S.I = Principal ,  Rate ,  Time : Principal * Rate * Time / 100
PrincipalAmount = 0
Rate = 0
Time = 0 

#Creating  Conditions and Taking User Input  
while PrincipalAmount <= 0:
    PrincipalAmount = float(input("Enter Principal Amount : "))
    if PrincipalAmount <= 0:
        print("Your Pricipal Must Greater Than Zero ")   
        
while Rate <= 0:
    Rate = float(input("Enter Interest Rate : "))
    print("Your Rate Is : ", Rate ,  "%")
    if Rate <= 0:
        print("Your Percentage Rate Must Be Greater Than Zero")  
        
while Time <= 0:
    Time = float(input("Enter Time Span : ")) 
    if Time <= 0:
        print("Your Time Span Must Be Greater Than Zero") 
         
SimpleInterest = PrincipalAmount * Rate * Time / 100 
print(f"Your Balance On Simple Interest  After {Time} Years Is : ${SimpleInterest: .2f} ")     
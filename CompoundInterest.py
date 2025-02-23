#Variables A = Fianl Amount ,  P = Initial Balance ,  r = Interest Rate , t = number of elapsed time 
print("Calculate Your Compound Interest Below ")
PrincipalAmount  = 0
Rate = 0 
Time = 0  

while PrincipalAmount <= 0:
    PrincipalAmount = float(input("Enter The Principal Amount : "))
    if PrincipalAmount <= 0: 
        print("Your Principal Amount Must  Be Greater Than Zero")

while Rate <= 0:
    Rate = float(input("Enter Interest Rate : "))
    print("Your Rate Is : " , Rate , "%")
    if Rate <= 0:
        print("Interest Rate Must Be Greater Than Zero")   
        
while Time <= 0:
    Time = float(input("Enter Time Spread Of Loan : "))
    if Time <= 0:
        print("Loan Time Must Be Greater Than Zero ")
    
CompoundInterest = PrincipalAmount * pow((1 + Rate / 100),Time)
print(f"Balance On Compound Interest After {Time} Years : ${CompoundInterest:.2f}")
#print(PrincipalAmount)
#print(Rate)
#print(Time)        
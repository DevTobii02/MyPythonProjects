#Hyp*2 = Opp*2 + Adj*2  
#Setting Parameters To Be Equal To Zero 
OppositeSide = 0
AdjacentSide = 0
HypotenuseSide = OppositeSide * OppositeSide + AdjacentSide * AdjacentSide

while OppositeSide <= 0:
    OppositeSide = int(input("Enter Value For Opposite Side : "))
    if OppositeSide <= 0:
        print("Opposite Side Cannot Be Greater  Than Zero")  
        
while AdjacentSide <= 0:
    AdjacentSide = int(input("Enter Value For Adjacent Side : ")) 
    if AdjacentSide <= 0:
        print("Adjacent Side Must Be Greater Than Zero") 
        
while HypotenuseSide <= 0:
    HypotenuseSide = int(input("Enter Value For Hypotenuse Side : ")) 
    if HypotenuseSide <= 0:
        print("Hypotenuse Side Must Be Greater Than Zero")       
        
if HypotenuseSide != OppositeSide * OppositeSide + AdjacentSide * AdjacentSide:
    print("Not A Pythagorean Equation")              
Num1 = int(input("Enter First Number : "))
Num2 = int(input("Enter Second Number : "))
Operator = input("Enter Operator : ") 

if Operator == "+":
    print("Your Result Is : ", Num1 + Num2)
    print(Num1 + Num2)
elif Operator == "-":
    print("Your Result Is : ", Num1 - Num2)
    print(Num1 - Num2) 
elif Operator == "*":
    print("Result Is : ", Num1 * Num2)  
    print(Num1 * Num2)
elif Operator == "/":
    print("Result Is : ", Num1 / Num2) 
    print(Num1 / Num2)
else:
    print("Invalid Operator")
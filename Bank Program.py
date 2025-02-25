import sys
import random
print("Welcome To My Bank")
users = {}
def GenerateAccountNumber():
    while True:
        AccountNumber = random.randint(1000000000, 9999999999)
        if not AccountNumberExists(AccountNumber):
            return AccountNumber 
def AccountNumberExists(AccountNumber):
    for user in users.values():
        if user['AccountNumber'] == AccountNumber:
            print("Account Number Exists")
            return True
        print("Account Number Does Not Exist")
        return False
def NewUser():
    while True:
        print("Fill In The Following Fields To Create An Account")
        Name = input("Enter Your Name : ")
        Age = 0
        Email = input("Enter Your Email : ")
        Password = input("Enter Your Password : ")
        ConfirmPassword = input("Confirm Your Password : ") 
        if Password != ConfirmPassword:
            print("Passwords Do Not Match , Please Try Again")
            continue
        try:
            Age = int(input("Enter Your Age : "))
            if Age > 17:
                    print("Account Created Successfully ")
                    return Name , Email
            else:
                    print("You Must Be 18 and Above To Open An Account On Your Own")             
                    sys.exit()
        except ValueError:
            print("Invalid Input") 
            continue                        
        AccountNumber = GenerateAccountNumber()
        print(f"Your Account Number is : {AccountNumber}")                                
def ExsistingUser():
    print("Fill In Your Login Details")
    Username = input("Enter Your Name : ")
    Email1  = input("Enter Your Email : ")
    print("Login Successfull!!!") 
    Activity = input(f"Choose An Activity (Deposit , Withdraw , Send Money , Check Balance , Save Money) : ").strip().lower()
    if Activity == "Deposit":
        DepositFunds() 
    elif Activity == "Withdraw":
        WithdrawFunds()
    elif Activity == "Send Money":
        SendMoney()
    elif Activity == "Check Balance":
        CheckBalance()
    elif Activity == "Save":
        Save()
    else:
        print("Invalid Operation")    
    return Username, Email1
Choice = input("Login or Sign Up : ").lower().strip()
if Choice == "Sign Up".lower().strip():
    NewUser()
elif Choice == "Login".strip().lower():
    ExsistingUser() 
    
else:
    print("Invalid Option")  
    
def DepositFunds():
    print("Fill In The Folllowing Transaction Details")
    
def WithdrawFunds():
    pass
def SendMoney():
    pass
def CheckBalance():
    pass
def Save():
    pass
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
                AccountNumber = GenerateAccountNumber()
                users[AccountNumber] = {
                    'Name' : Name,
                    'Age' : Age,
                    'Email' : Email,
                    'Password' : Password,
                    'AccountNumber' : AccountNumber,
                    'Balance' : 0
                }
                print(f"Your Account Number is : {AccountNumber}")
                print("Account Created Successfully ")
                return Name , AccountNumber
            else:
                    print("You Must Be 18 and Above To Open An Account On Your Own")             
                    sys.exit()
        except ValueError:
            print("Invalid Input, Expected An Integer Value") 
            continue          
        
                                                   
def ExistingUser():
    print("Fill In The Following Fields To Login")
    try:
        AccountNumber = int(input("Enter Your Account Number : "))
    except ValueError:
        print("Invalid Account Number, Series Of Numbers Expected")
        return
    Password = input("Enter Your Password : ") 
    if AccountNumber in users:
        if Password == users[AccountNumber]['Password']:
            print("Login Successful")
            return AccountNumber   
        else:
            print("Invalid Password")
    else:
        print("Account Number Does Not Exist")
        return None
        
def DepositFunds():
    pass
def WithdrawFunds():
    pass
def SendMoney():
    pass
def CheckBalance():
    pass
def Save():
    pass 
Choice = input("Login or Sign Up : ").lower().strip()
if Choice == "Sign Up".lower().strip():
    NewUser()
    ExistingUser()
elif Choice == "Login".lower().strip():
    ExistingUser()
else:
    print("Inavalid Choice")  
   
Activity = input("What Would You Like To Do : Deposit , Withdraw , Send Money , Check Balance : ").lower().strip()
if Activity == "Deposit".lower().strip():
    DepositFunds()
elif Activity == "Withdraw".lower().strip():
    WithdrawFunds()
elif Activity == "Send Money".lower().strip():
    SendMoney()
elif Activity == "Check Balance".lower().strip():
    CheckBalance()
else:
    print("Invalid Activity")    
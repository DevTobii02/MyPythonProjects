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
                    'Balance' : 0.0
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
        return None
    Password = input("Enter Your Password : ") 
    if AccountNumber in users:
        if Password == users[AccountNumber]['Password']:
            print("Login Successful")
            return AccountNumber   
        else:
            print("Invalid Password")
    else:
        print("Account Number Does Not Exist")
        sys.exit()
        return None
       
def DepositFunds(AccountNumber):
    if AccountNumber:
        AmountToBeDeposited = float(input("Enter Amount To Be Deposited  : "))
        if AmountToBeDeposited > 0:
            users[AccountNumber]['Balance'] += AmountToBeDeposited
            print(f"Deposit Successful. New Balance: {users[AccountNumber]['Balance']:.3f}")
        else:
            print("Invalid Amount. Please Enter A Positive Number.")
    else:
        print("Deposit Failed. Please Try Again.")
        
def WithdrawFunds(AccountNumber):
    AccountNumber = ExistingUser()
    if AccountNumber:
        AmountToBeWithdrawn = float(input("Enter Amount To Be Withdrawn : "))
        if AmountToBeWithdrawn < 0:
            print("Amount To Be Withdrawn Must Be Greater Than 0")
        elif users[AccountNumber]['Balance'] >=  AmountToBeWithdrawn:
            users[AccountNumber]['Balance'] -= AmountToBeWithdrawn
            print(f"Withdrawal Successful. New Balance: {users[AccountNumber]['Balance']:.3f}")
        else:
            print("Insufficient Funds")
    else:
        print("Withdrawal Failed. Please Try Again.")
        
def CheckBalance(AccountNumber):
    if AccountNumber:
        print(f"Your Account Balance is : {users[AccountNumber]['Balance']:.3f}")
    else:
        print("Invalid Account Number")
def PrintInfo():
    for UserAccountNumber, User in users.items():
        print(f"Account Number : {UserAccountNumber}")
        for key, value in User.items():
            print(f"{key} : {value}")
            
Choice = input("Login or Sign Up : ").lower().strip()
if Choice == "Sign Up".lower().strip():
    name, AccountNumber = NewUser()
    AccountNumber = ExistingUser()
elif Choice == "Login".lower().strip():
   AccountNumber = ExistingUser()
else:
    print("Inavalid Choice")  

if AccountNumber:
    while True:
        Activity = input("What Would You Like To Do : Deposit , Withdraw , Send Money , Check Balance , Print Info : ").lower().strip()
        if Activity == "Deposit".lower().strip():
            DepositFunds(AccountNumber)
        elif Activity == "Withdraw".lower().strip():
            WithdrawFunds(AccountNumber)
        elif Activity == "Check Balance".lower().strip():
            CheckBalance(AccountNumber)
        elif Activity == "Print Info".lower().strip():
            PrintInfo()
        elif Activity == "Exit".lower().strip():
            print("Thank You For Banking With Us")  
            sys.exit()  
        else:
            print("Invalid Activity")  
else:
    print("Failed Login")  
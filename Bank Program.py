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
            print("Invalid Input") 
            continue                                                     
def ExsistingUser():
    print("Fill In Your Login Details")
    Username = input("Enter Your Name : ")
    Email1  = input("Enter Your Email : ")
    password = input("Enter Your Password : ")
    for AccountNumber, user in users.items():
        if user['Name'] == Username and user['Email'] == Email1 and user['Password'] == password:
            print("Login Successfull!!!") 
            Activity = input(f"Choose An Activity (Deposit , Withdraw , Send Money , Check Balance , Save Money) : ").strip().lower()
    if Activity == "Deposit".strip().lower():
        DepositFunds(AccountNumber) 
    elif Activity == "Withdraw":
        WithdrawFunds(AccountNumber)
    elif Activity == "Send Money":
        SendMoney(AccountNumber)
    elif Activity == "Check Balance":
        CheckBalance(AccountNumber)
    elif Activity == "Save":
        Save(AccountNumber)
    else:
        print("Invalid Operation")
    return Username, AccountNumber 
    
def DepositFunds(AccountNumber):
    AccountNumber = int(input("Enter Your Account Number : "))
    Amount = float(input("Enter Amount To Be Deposited : "))  
    users[AccountNumber]['Balance'] += Amount
    print(f"The Amount Of {Amount} Has Been Deposited Successfully Into Your Account")
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
elif Choice == "Login".strip().lower():
    ExsistingUser()     
else:
    print("Invalid Option")  

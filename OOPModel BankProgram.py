import sys
import random 
import datetime
print("Welcome To Our Bank")
Date = datetime.datetime.now()
print(Date)
class Account:
    def __init__(self, Name, Age, Email, Password, AccountNumber, Balance): 
        self.Name = Name
        self.Age = Age
        self.Email = Email
        self.Password = Password
        self.AccountNumber = AccountNumber
        self.Balance = 0.0
    
    def Deposit(self, Amount):
        if Amount > 0:
            self.Balance += Amount
            print("Amount Deposited: ", Amount)
            print("New Balance: ", self.Balance)
        else:
            print("Insufficient Amount")
    
    def Withdraw(self, Amount):
        if Amount <= 0:
            print("Amount To Be Withdrawn Must Be Greater Than Zero")
        elif self.Balance >= Amount:
            self.Balance -= Amount
            print("Amount Withdrawn: ", Amount) 
            print(f"Your Withdrawal Was Successfull. New Balance Is : {self.Balance:.2f} ")
        else:
            print("You Have Insufficient Funds")   
             
    def CheckBalance(self):
        print(f"Your Current Balance Is: {self.Balance:.2f}")
    
    def PrintInfo(self):
        print("Your Account Information")
        print(f"Account Number: , {self.AccountNumber}")
        print(f"Name: , {self.Name}")
        print(f"Age: , {self.Age}")
        print(f"Email: , {self.Email}")
        print(f"Balance: , {self.Balance}")
    
class Bank:
    def __init__(self):
        self.Customers = {}
    
    def GenerateAccountNumber(self):
        while True:
            AccountNumber = random.randint(1000000000, 9999999999)
            if AccountNumber not in self.Customers:
                return AccountNumber
    
    def NewUser(self):
        while True:
            print("Fill In The Following Fields To Create An Account")
            Name = input("Enter Your Name : ")
            Age = 0
            Email = input("Enter Your Email : ")
            Password = input("Enter Your Password : ")
            ConfirmPassword = input("Confirm Your Password : ")
            if Password != ConfirmPassword:
                print("Passwords Do Not Match")
                continue
            try:
                Age = int(input("Enter Your Age : "))
                if Age <= 17:
                    print("Cannot Open An Account, You Must Be 18 and Above")
                    sys.exit()
                else:
                    AccountNumber = self.GenerateAccountNumber()
                    NewlyGeneratedAccount = Account(Name, Age, Email, Password, AccountNumber, 0.0)
                    self.Customers[AccountNumber] = NewlyGeneratedAccount  
                    print(f"Your Account Number Is : {NewlyGeneratedAccount.AccountNumber}")
                    print("Account Created Successfully")   
                    print("You Are Now Logged In")
                    return NewlyGeneratedAccount
            except ValueError:
                print("Invalid Input, An Integer Value Expected")
                return None
            
    def ExsistingUser(self):
        print("Fill In The Following Fields To Login")  
        try:
            AccountNumber = int(input("Enter Your Account Number : "))
        except ValueError:
            print("Invalid Account Number ,  Series Of Numbers Expected")
            return None
        Password = input("Enter Your Password : ")
        if AccountNumber in self.Customers:
            if self.Customers[AccountNumber].Password == Password:
                print("Login Successful")
                return AccountNumber
            else:
                print("Invalid Password")
                return None
        else:
            print("Account Does Not Exist")
            return None 
        
    def MenuList(self):
        Choice = input("Login or Sign up : ").lower().strip()
        if Choice == "Sign Up".lower().strip():
           AccountNumber =  self.NewUser()
        elif Choice == "Login".lower().strip():
            AccountNumber = self.ExsistingUser()
        else:
            print("Invalid Choice")
            return 
        
        if AccountNumber:
            account = self.Customers[AccountNumber]
            while True:
                Activity = input("What Activity Do You Want To Carry Out (Deposit, Withdraw, Check Balance, Exit) ? : ").lower().strip()
                if Activity == "deposit":
                    Amount = float(input("Enter Amount To Be Deposited :"))
                    account.Deposit(Amount)
                elif Activity == "withdraw":
                    Amount = float(input("Enter Amount To Be Withdrawn : "))    
                    account.Withdraw(Amount)
                elif Activity == "check balance":
                    account.CheckBalance()
                elif Activity == "exit":
                    print("Exiting...")
                    break
                else:
                    print("Invalid Activity")
        else:
            print("Invalid Account Number")  
            
print(Date)
MyBank = Bank()
MyBank.MenuList()                  
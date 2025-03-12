import sys
import random 
import datetime
import sqlite3
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
        print(f"Deposit Action At {Date}")        
    
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
        print(Date)
    
    def PrintInfo(self):
        print("Your Account Information")
        print(f"Account Number: {self.AccountNumber}")
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Email: {self.Email}")
        print(f"Balance: {self.Balance:.2f}")
        print(Date)
    
class Bank:
    def __init__(self):
        self.Customers = {}
        self.conn = sqlite3.connect("Bank.db")
        self.cursor = self.conn.cursor() 
            
    def CreateTable(self):
        # Create a table for storing customer information if it doesn't already exist
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers(
            Name TEXT,
            Age INTEGER,
            Email TEXT,
            Password TEXT,
            AccountNumber INTEGER PRIMARY KEY,
            Balance REAL
        )
        """)
        self.conn.commit()

    def SaveCustomer(self, account):
        # Insert a new customer record into the database
        self.cursor.execute("""
        INSERT INTO Customers (Name, Age, Email, Password, AccountNumber, Balance)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (account.Name, account.Age, account.Email, account.Password, account.AccountNumber, account.Balance))
        self.conn.commit()

    def GetCustomer(self, account_number):
        # Retrieve a customer record from the database based on the account number
        self.cursor.execute("SELECT * FROM Customers WHERE AccountNumber = ?", (account_number,))
        customer = self.cursor.fetchone()
        if customer:
            name, age, email, password, account_number, balance = customer
            return Account(name, age, email, password, account_number, balance)
        else:
            return None

            
            
    def GenerateAccountNumber(self):
        while True:
            AccountNumber = random.randint(1000000000, 9999999999)
            if AccountNumber not in self.Customers:
                return AccountNumber
    print(Date)    
    
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
                    print(f"Your Account Was Created At {Date}")
                    print(Date)
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
                print(f"Logged In At {Date}")
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
           account = self.NewUser()
           if account:
            AccountNumber = self.ExsistingUser()
           else:
               return
        elif Choice == "Login".lower().strip():
            AccountNumber = self.ExsistingUser()
        else:
            print("Invalid Choice")
            return 
        
        if AccountNumber:
            account = self.Customers[AccountNumber]
            while True:
                Activity = input("What Activity Do You Want To Carry Out (Deposit, Withdraw, Check Balance, Print Info,  Exit) ? : ").lower().strip()
                if Activity == "deposit":
                    Amount = float(input("Enter Amount To Be Deposited :"))
                    account.Deposit(Amount)
                elif Activity == "withdraw":
                    Amount = float(input("Enter Amount To Be Withdrawn : "))    
                    account.Withdraw(Amount)
                elif Activity == "check balance":
                    account.CheckBalance()
                elif Activity == "print info":
                    account.PrintInfo() 
                elif Activity == "exit":
                    print("Exiting...")
                    print(Date)
                    break
                else:
                    print("Invalid Activity")
        else:
            print("Invalid Account Number")  
                 
if __name__ == "__main__":
    MyBank = Bank()
    MyBank.MenuList()
    
    
    
    
    """
    # Close the database connection when the program exits
    def __del__(self):
        self.conn.close()

    # Add the following methods to the Bank class
    """
    """
    def CreateTable(self):
        # Create a table for storing customer information if it doesn't already exist
        self.cursor.execute("""
    """CREATE TABLE IF NOT EXISTS Customers(
            Name TEXT,
            Age INTEGER,
            Email TEXT,
            Password TEXT,
            AccountNumber INTEGER PRIMARY KEY,
            Balance REAL
        )
        )"""
    """self.conn.commit()
        """   
    """
    def SaveCustomer(self, account):
        # Insert a new customer record into the database
        """
    ""    """self.cursor.execute("""
    """INSERT INTO Customers (Name, Age, Email, Password, AccountNumber, Balance)
        VALUES (?, ?, ?, ?, ?, ?)
        """,""" (account.Name, account.Age, account.Email, account.Password, account.AccountNumber, account.Balance))
        self.conn.commit()
        """
    """
    def GetCustomer(self, account_number):
        # Retrieve a customer record from the database based on the account number
        self.cursor.execute("SELECT * FROM Customers WHERE AccountNumber = ?", (account_number,))
        customer = self.cursor.fetchone()
        if customer:
            name, age, email, password, account_number, balance = customer
            return Account(name, age, email, password, account_number, balance)
        else:
            return None

    # Update the NewUser method to save the new customer to the database
    def NewUser(self):
        while True:
            print("Fill In The Following Fields To Create An Account")
            name = input("Enter Your Name : ")
            age = 0
            email = input("Enter Your Email : ")
            password = input("Enter Your Password : ")
            confirm_password = input("Confirm Your Password : ")
            if password != confirm_password:
                print("Passwords Do Not Match")
                continue
            try:
                age = int(input("Enter Your Age : "))
                if age <= 17:
                    print("Cannot Open An Account, You Must Be 18 and Above")
                    sys.exit()
                else:
                    account_number = self.GenerateAccountNumber()
                    newly_generated_account = Account(name, age, email, password, account_number, 0.0)
                    self.Customers[account_number] = newly_generated_account
                    self.SaveCustomer(newly_generated_account)  # Save the new customer to the database
                    print(f"Your Account Number Is : {newly_generated_account.AccountNumber}")
                    print("Account Created Successfully")
                    print("You Are Now Logged In")
                    print(f"Your Account Was Created At {Date}")
                    print(Date)
                    return newly_generated_account
            except ValueError:
                print("Invalid Input, An Integer Value Expected")
                return None

    # Update the ExsistingUser method to retrieve the customer from the database
    def ExsistingUser(self):
        print("Fill In The Following Fields To Login")
        try:
            account_number = int(input("Enter Your Account Number : "))
        except ValueError:
            print("Invalid Account Number, Series Of Numbers Expected")
            return None
        password = input("Enter Your Password : ")
        account = self.GetCustomer(account_number)  # Retrieve the customer from the database
        if account:
            if account.Password == password:
                print("Login Successful")
                print(f"Logged In At {Date}")
                self.Customers[account_number] = account  # Add the account to the in-memory dictionary
                return account_number
            else:
                print("Invalid Password")
                return None
        else:
            print("Account Does Not Exist")
            return None
"""
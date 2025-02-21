print("Welcome To Our Banking System")
UserMode = input("Select User Mode : ").strip().capitalize()
if UserMode == "Customer":
    print("What activity will you be carrying out")
    ListOfActivities = ["1. Register New Customer", "2. Create New Account",  "3. Deposit Funds","4. Withdraw Funds","5. Send Money", "6. View My Details "]
    for activity in ListOfActivities:
        print(activity)
    ChooseActivities = print(input("Choose From The Above Listed Activities : "))
elif UserMode == "Banker":
    print("Welcome To Bankers Section Provide Your Work  Details")  
else:
    print("Invalid Mode") 





























    
"""    
class Bank:  
    def __init__(self):
        self.Customers = {}    
    def CreateCustomer(self, Name, Password, Balance=0 ) :
        if Name in self.Customers:
            print(f"Customer with the name {Name} already exist")
        else:
            self.Customers[Name] = Customer(Name, Password, Balance) 
            print(f"Account Created Successfully for {Name} with Balance ")
    def GetCustomer(self, Name, Password):
        Customer = self.Customers.get(Name)
        if Customer and Customer.Password == Password:
            print(f"Welcome Back {Name}!") 
            return Customer
        else:
            print("Invalid Name or Password") 
            return None
    """        
    
    

"""      
class Customer:
    def __init__(self,Name, Password, Balance = 0.0):
        self.Name = Name
        self.Password = Password
        self.Balance = Balance
        self.Transaction = []  
    def DepositFunds(self, Amount):
        if Amount <=0:
            print("Deposit Must be Positive")
            return
        self.Balance += Amount
        self.Transactions.append(f"Deposited ${Amount: .2f}")
        print(f"{self.Name}, You have deposite ${Amount: .2f}")
    
    def WithdrawFunds(self, Amount):
        if Amount <= 0:
            print("Withdraw Value Must Positive") 
            return
        if Amount > self.Balance:
            print("Insufficient Funds") 
        else:
            self.Balance -= Amount 
            self.Transaction.append(f"Withdrew ${Amount: .2f}")
            print(f"{self.Name}, You Have Withdrawn ${Amount} ") 
    def SendMoney(self, Receipient, Amount):
        if Amount <= 0:
            print("Transfer Must Be Positive") 
            return
        if Amount > self.Balance:
            print("Insufficient Funds To Send Money.") 
        else:
            self.Balance -= Amount
            Receipient.Balance += Amount
            self.Transaction.append(f"Sent ${Amount: .2f} To {Receipient.Name}")
            Receipient.Transaction.Append(f"")  
        """
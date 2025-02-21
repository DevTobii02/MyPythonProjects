class Customer():
    def __init__(self, Name, AccountNumber, Age, Gender, ContactNo):
        self.Name = Name
        self.AccountNumber = AccountNumber
        self.Age = Age 
        self.Gender = Gender
        self.ContactNo = ContactNo 
        
    def ShowCustomerDetails(self):
        print("Customer Details Are As Follows : .....")
        #print(" ")
        print("Name = ", self.Name)
        print("AccountNumber = ", self.AccountNumber)
        print("Age = ", self.Age)
        print("Gender = ", self.Gender)
        print("ContactNo = ", self.ContactNo)  
        
class Bank(Customer):
    def __init__(self, Name,AccountNumber,  Age, Gender, ContactNo):
        super().__init__(Name, AccountNumber, Age, Gender, ContactNo) 
        self.Balance = 0 
    
    def DepositTransaction(self, Amount):
        self.Amount = Amount 
        self.Balance = self.Balance + self.Amount
        print("Your Account Balance Is Credited by:$",self.Amount)
        print("Your Account Balance Is:$",self.Balance) 
        
    def WithdrawTransaction(self, Amount):
        self.Amount = Amount
        if self.Amount > self.Balance:
            print("Sorry Insufficient Balance ")
            print("Your Available Balance is: $",self.Balance) 
        else:
            self.Balance = self.Balance - self.Amount
            print("Your Account Is Debited By:  ", self.Amount) 
            print("Your Account Balance Is : $ ",self.Balance )   
            
    def CheckBalance(self):
        print("Your Account Balance Is $ : ", self.Balance)               
        
CreateCustomer = Customer("Dave", 3084256789,  20, "Male", 8045267865) 
Customer1 = Bank("Dave", 3054647828, 27, "Male", 80925683388)
Customer1.ShowCustomerDetails()
Customer1.DepositTransaction(1000)
Customer1.WithdrawTransaction(2000)
#CreateCustomer.ShowCustomerDetails()       
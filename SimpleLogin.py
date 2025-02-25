users = {}  
def SignUp():
    print("Fill In The Following Fields To Sign Up Now")
    SignUp_Username = input("Enter A Username : ")
    SignUp_Password = input("Enter A Password : ") 
    users[SignUp_Username] = SignUp_Password
    print("Sign Up Successfull, Kindly Proceed To Login")

def Login():
    print("Login") 
    print("Please Provide Correct Information To The Following Fields") 
    Login_Username = input("Enter Your Login Username : ") 
    Login_Password = input("Provide Your Correct Password : ") 
    if Login_Username in users and Login_Password == users[Login_Username]:
        print(f"Login Successfull Welcome Back , {Login_Username}")
        Activity = input(f"Choose An Activity (Deposit , Withdraw , Send Money , Check Balance , Save Money) : ").strip().lower()
        if Activity == "Deposit":
            DepositFunds()
        elif Activity == "Withdraw":
            WithdrawFunds()
        elif Activity == "Send Money":
            SendMoney()
        elif Activity == "Check Balance":
            CheckBalance()
        elif Activity == "Save Money":
            SaveMoney()
        else:
            print("Invalid Request")
    else:
        print("Invalid Username or Password")  
        
def DepositFunds():
    pass
def WithdrawFunds():
    pass
def SendMoney():
    pass        
def CheckBalance():
    pass
def SaveMoney():
    pass
print("Welcome !!! (Sign Up or Login)") 
Choice = input("Login or Sign Up : ").strip().lower() 
if Choice == "Sign Up".strip() .lower():
    SignUp()
    Login()
elif Choice == "Login":
    Login()
else:
    print("Invalid Choice")      
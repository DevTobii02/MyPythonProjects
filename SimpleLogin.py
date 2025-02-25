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
print("Welcome !!! (Sign Up or Login)") 
Choice = input("Login or Sign Up : ").strip().lower() 
if Choice == "Sign Up".strip() .lower():
    SignUp()
    Login()
elif Choice == "Login":
    Login()
else:
    print("Invalid Choice")      
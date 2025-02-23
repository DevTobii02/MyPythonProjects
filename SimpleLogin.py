print("Welcome") 

Choice = input("Enter Your Choice (Login or Sign Up) : ") 

if Choice .strip() .lower() == "Sign Up":
    print("Fill In The Following Fields To Sign Up")
    Username = input("Enter A Valid Username : ")
    Password = input("Provide A Valid Password : ")
    print("Account Created Successfully")
    print("Proceed To Login Now !!!")
elif Choice == "Login":
    print("Fill In The Following Fields With The Correct Information")  
    Username1 = input("Enter Your username : ") 
    Password1 = input("Enter Your password : ")
if Username == Username1 and Password == Password1:
    print("Logged In Succesfully")
else:
    print("Invalid username or password ")

    
if Username == Username1 and Password == Password1:
    print("Logged In Succesfully")
else:
    print("Invalid username or password ")
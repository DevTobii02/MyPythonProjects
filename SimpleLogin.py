print("Welcome")
Choice = input("Choose An Option (Login or Sign Up) : " ) .strip() 
if Choice == "Sign Up": 
    print("Fill In  Information To The Fields Below")
    UserName = input("Enter A Valid UserName : ")
    PassWord = input("Create A Strong/Valid Password : ") 
    print("Accout Created Succesfully")  
    print("Please Login In Now !!!")  
elif Choice == "Login":
    print("Provide Correct Information To The Following Fields")
    username = input("Enter Your Username : ") 
    password = input("Enter Your Password : ") 
else:
    print("Wrong Input") 

if UserName == username and PassWord == password: 
    print("Logged In Successfully")    
else:
    print("Invalid Username or Password")
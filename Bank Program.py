#Create New User and Login New User
print("Welcome To Our Bank Program")
Option = input("Enter Your Choice (Login or Sign Up ) ? : ")

if Option.lower()  == "Sign Up":  
    Name = input("Enter Your Name : ")  
    Email = input("Enter Your Email : ")
    Password = input("Create A Strong/Valid Password : ") 
    Age = 0
    while Age <= 0:
        Age = int(input("Enter Your Age : "))
        if Age <= 17:
            print("Too Young Too Open Account On Your Own")
        else:
            print("Account Created Successfully")  
    print("Proceede To Login Now!!!") 
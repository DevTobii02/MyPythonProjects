import datetime
import random
import sys

Students = {}  #Initializes A Dictionary To Keep Trcak Pf Student Data 
Date = datetime.datetime.now()
print(Date)
 
 
def GenerateRegistrationNumber():
    if ChooseDepartment == "Science":
        RegistrationNumber = random.randint(1000, 1999)
    elif ChooseDepartment == "Arts":
        RegistrationNumber = random.randint(2000, 2999)
    elif ChooseDepartment == "Commercial":
        RegistrationNumber = random.randint(3000, 4000) 
    else:
        print("Invalid Department")
        return None
    return RegistrationNumber  


def RegisterNewStudent():
    print("New Student Registration")
    Name = input("Enter Your Name : ")
    Age = 0
    Email = input("Enter Your Email : ")
    Age = int(input("Enter Your Age : "))
    if Age > 2 and Age > 18:
        print("Does Not Fit Too Age Criteria")

        
def CheckRegistrationNumber():
    pass

def RegisteredStudent(): 
    print("Fill The Following Fields With Your Correct Details")
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    

def ScienceDepartment():
    pass

def ArtsDepartment():
    pass

def CommercialDepartment():
    pass

Choice = input("New or Returning Students : ").lower().strip()
if Choice == "New".lower().strip():
    RegisterNewStudent()
elif Choice == "Returning Student".lower().strip():
    RegisteredStudent()
       

ChooseDepartment = input("Enter Choose Your Department : ")
if ChooseDepartment == "Science":
    ScienceDepartment()
elif ChooseDepartment == "Arts":
    ArtsDepartment()
elif ChooseDepartment == "Commercial":
    CommercialDepartment()        

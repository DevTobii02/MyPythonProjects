import datetime
import random
import sys

Students = {}  #Initializes A Dictionary To Keep Trcak Pf Student Data 
Date = datetime.datetime.now()
print(Date)
 
  
def GenerateRegistrationNumber(ChooseDepartment):  #Generates Registration Number Based On Department
    if ChooseDepartment == "Science":
        RegistrationNumber = random.randint(1000, 1999)
    elif ChooseDepartment == "Arts":
        RegistrationNumber = random.randint(2000, 2999)
    elif ChooseDepartment == "Commercial":
        RegistrationNumber = random.randint(3000, 3999) 
    else:
        print("Invalid Department")
        return None
    return RegistrationNumber  

def RegisterNewStudent():
    print("New Student Registration")
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    Age = int(input("Enter Your Age : "))
    if Age < 2 or Age > 18:
        print("Does Not Fit Too Age Criteria")   
        return  #Use to exit the function early if conditions are not met  
    ChooseDepartment = input("Enter Your Department : ").strip().capitalize()
    RegistrationNumber = GenerateRegistrationNumber(ChooseDepartment)
    print(RegistrationNumber) 
    print("New Student Successfully Registered")
    if RegistrationNumber is None:
        print("Failed To Generate Registration Number") 
        
def CheckRegistrationNumber():
    if GenerateRegistrationNumber in Students:
        print("Student Already Exists")

def RegisteredStudent(): 
    print("Fill The Following Fields With Your Correct Details")
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    

def ScienceDepartment():
    Subjects = ["English Language", "Mathematics", "Physics", "Chemistry", "Biology", "Further Mathematics" ,"Information  Communication Technology",  "Data Processing", "Geography", "Economics"]        
    Teachers = ["1.Mr.John = Mathematics", "2. Mr.James = English Language", "3.Mr. Peter = Physics", "4.Mr. Paul = Chemistry", "5. Mr.Jude =  Further Mathematics", "6.Mr.Joseph = Inforation Communication Technology", "7. Mr. Emmanuel = Data Processing", "8. Mr World = Geography", "9.Mr Kingsley = Economics"]         
    TeachersorSubjects = input("What Do You Want To Get (Subjects or Teachers ) ? : ")    
    if TeachersorSubjects.lower().strip() == "teachers":
        for teacher in Teachers:
            print(teacher) 
    elif TeachersorSubjects.lower().strip() == "subjects":
        for subject in Subjects:
            print(subject)      
    else:
        print("Invalid Input")             
            
def ArtsDepartment():
    Subjects = ["Engish Language", "Mathematics", "Literature In English", "Government", "Islamic Religious Studies", "Christian Religious Studies", "Civic Education",  "History", "Visual Arts", "Music", "French", "Yoruba", "Igbo", "Hausa"]
    Teachers = ["1. Mr. Remi = English Language", "2. Mr Bright = Mathematics", "3. Mrs. Funmi = Literature In English", "4. Mr. John = Government", "5. Mr. Ibrahim  = Islamic Religious Studies", "6. Mr. Paul = Christian Religious Studies", "7. Mr. Jude = Civic Education", "8. Mrs. Grace = History", "9. Mr. Emmanuel = Visual Arts", "10. Mrs. Rose = Music", "11. Mr. Joseph = French", "12. Mrs. Funke = Yoruba", "13. Mrs. Ngozi = Igbo", "14. Mrs. Amina = Hausa"]
    TeachersorSubjects = input("What Do You Want To Get (Subjects or Teachers) ? : ") 
    if TeachersorSubjects.lower().strip() == "teachers":
        for teacher in Teachers:
            print(teacher)  
    elif TeachersorSubjects.lower().strip() == "subjects":
        for subject in Subjects:
            print(subject)
    else:
        print("Invalid Input")  
        
def CommercialDepartment():
    Subjects = ["English Language", "Mathematics", "Economics" "Financial Accounting", "Commerece", "Economics", "Further Mathematics", "Book Keeping"]
    Teachers = ["1.Mrs Anna = English Language"]
    TeachersorSubjects = input("What Do To Get (Subjects or Teachers) ? :") 
    if TeachersorSubjects:
        for teacher in Teachers:
            print(teacher) 
    elif TeachersorSubjects:
        for subject in Subjects:
            print(subject)        
    
def PrintStudentDetails():
    if GenerateRegistrationNumber in Students:
        print(f"Name : {Students[GenerateRegistrationNumber]['Name']}")
        print(f"Age : {Students[GenerateRegistrationNumber]['Age']}")
        print(f"Email : {Students[GenerateRegistrationNumber]['Email']}")
        print(f"Registration Number : {Students[GenerateRegistrationNumber]['RegistrationNumber']}")
        print(f"Department : {Students[GenerateRegistrationNumber]['ChooseDepartment']}")
        print(f"Your Subjects Are : {Students[GenerateRegistrationNumber]['Subjects']}")
        print(f"Date Of Registration : {Students[GenerateRegistrationNumber]['DateOfRegistration']}")
    else:
        print("Student Does Not Exist")  
               
Choice = input("New or Returning Students : ").lower().strip()
if Choice == "New".lower().strip():
    RegisterNewStudent()
elif Choice == "Returning Student".lower().strip():
    RegisteredStudent()
elif Choice == "Print Info".lower().strip():
    PrintStudentDetails()
else:
    print("Invalid Input")    
           

ChooseDepartment = input("Enter Choose Your Department : ").strip() .lower()
if ChooseDepartment == "Science".lower().strip():
    ScienceDepartment()
elif ChooseDepartment == "Arts".lower().strip():
    ArtsDepartment()
elif ChooseDepartment == "Commercial":
    CommercialDepartment()        
else:
    print("Not A Department")    
    
    
    
    
  
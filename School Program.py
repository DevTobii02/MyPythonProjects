import datetime
import random
import sys

Students = {}  #Initializes A Dictionary To Keep Trcak Pf Student Data 
Date = datetime.datetime.now()
print("Welcome My School")
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
    print("New Student Registration, Fill in the following")
    Name = input("Enter  Your Name : ")
    Email = input("Enter Your Email : ")
    Age = int(input("Enter Your Age : "))
    if Age < 2 or Age > 18:
        print("Does Not Fit Too Age Criteria") 
        sys.exit()  
        return  #Use to exit the function early if conditions are not met  
    ChooseDepartment = input("Enter Your Department : ").strip().capitalize()
    RegistrationNumber = GenerateRegistrationNumber(ChooseDepartment)
    if RegistrationNumber is None:
        print("Failed To Generate Registration Number") 
        return #Use to exit the function early if conditions are not met  
    if ChooseDepartment == "Science":
        Subjects = ["1.English Language", "2.Mathematics", "3.Physics", "3.Chemistry", "4.Biology", "5.Further Mathematics", "6.Information Communication Technology", "7.Data Processing", "8.Geography", "9.Economics"]
    elif ChooseDepartment == "Arts":
        Subjects = ["1.English Language", "2.Mathematics", "3.Literature In English", "4.Government", "5.Islamic Religious Studies", "6.Christian Religious Studies", "7.Civic Education", "8.History", "9.Visual Arts", "10.Music", "11.French", "12.Yoruba", "13.Igbo", "14.Hausa"]
    elif ChooseDepartment == "Commercial":
        Subjects = ["1.English Language", "2.Mathematics", "3.Economics", "4.Financial Accounting", "5.Commerce", "6.Further Mathematics", "7.Book Keeping", "8.Data Processing"]
    else:
        Subjects = []

    Students[Email] = {
        "Name" : Name,
        "Email" : Email,
        "Age" : Age,
        "ChooseDepartment" : ChooseDepartment,
        "RegistrationNumber" : RegistrationNumber,
        "DateOfRegistration" : datetime.datetime.now(),
        "Subjects" : Subjects
    }
    print("New Student Registered Successfully")
    print(f"Your Registration Number Is : {RegistrationNumber}")
        
def CheckRegistrationNumber():
    Email = input("Enter Your Email : ")
    if Email  in Students:
        print("Student Already Exists")
    else:
        print("No Record Of Student With This Email")

def RegisteredStudent(): 
    print("Fill The Following Fields With Your Correct Details")
    Name = input("Enter Your Name : ")
    Email = input("Enter Your Email : ")
    if Email in Students:
        print("Student Already Exists")
    else:
        print("Student Does Not Exist")

def ScienceDepartment():
    Subjects = ["1.English Language", "2.Mathematics", "3.Physics", "4.Chemistry", "5.Biology", "6.Further Mathematics" ,"7.Information  Communication Technology",  "8.Data Processing", "9.Geography", "10.Economics"]        
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
    Subjects = ["1.Engish Language", "2.Mathematics", "3.Literature In English", "4.Government", "5.Islamic Religious Studies", "6.Christian Religious Studies", "7.Civic Education",  "8.History", "9.Visual Arts", "10.Music", "11.French", "12.Yoruba", "13.Igbo", "14.Hausa"]
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
    Subjects = ["1.English Language", "2.Mathematics", "3.Economics" "4.Financial Accounting", "5.Commerece", "6.Economics", "7.Further Mathematics", "8.Book Keeping", "9.Data Processing"]
    Teachers = ["1.Mrs Anna = English Language", "2. Mr Benard = Mathematics", "3. Mr Kingsley = Economics", "4. Mr. Paul = Financial Accounting", "5. Mr. Jude = Commerece", "6. Mr. Joseph = Further Mathematics", "7. Mr. Emmanuel = Book Keeping", "8. Mr Mathew = Data Processing"]
    TeachersorSubjects = input("What Do To Get (Subjects or Teachers) ? :") 
    if TeachersorSubjects.lower().strip() == "teachers":
        for teacher in Teachers:
                print(teacher)
    elif TeachersorSubjects.lower().strip() == "subjects":
        for subject in Subjects:
            print(subject)
    else:
        print("Invalid Input")
              
    
def PrintStudentDetails():
    Email = input("Enter Your Email : ")
    if Email in Students:
        student = Students[Email]
        print(f"Name : {student['Name']}")
        print(f"Age : {student['Age']}")
        print(f"Email : {student['Email']}")
        print(f"Registration Number : {student['RegistrationNumber']}")
        print(f"Department : {student['ChooseDepartment']}")
        print(f"Your Subjects Are : ")
        for subject in student['Subjects']:
            print(f"- {subject}")
        print(f"Date Of Registration : {student['DateOfRegistration']}")
    else:
        print("Student Does Not Exist")  

                             
if __name__ == "__main__":
    while True:
        Choice = input("New or Returning Students or print info : ").lower().strip()
        if Choice == "new":
            RegisterNewStudent()
        elif Choice == "returning student":
            RegisteredStudent()
        elif Choice == "print info":
            PrintStudentDetails() 
        elif Choice == "check registration number":
            CheckRegistrationNumber() 
        elif Choice == "exit":
                print("Exiting The Program")
                sys.exit()

        ChooseDepartment = input("Enter Choose Your Department : ").strip().lower()
        if ChooseDepartment == "science":
            ScienceDepartment()
        elif ChooseDepartment == "arts":
            ArtsDepartment()
        elif ChooseDepartment == "commercial":
            CommercialDepartment()
        else:
            print("Not A Department")

        continue_program = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_program != "yes":
            break
                
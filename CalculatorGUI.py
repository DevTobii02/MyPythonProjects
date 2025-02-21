# Building A Calculator GUI 
from tkinter import *
root = Tk()
root.title("Simple Calculator") # Gives The GUI Interface A Title 
root.config(background="Skyblue")
a = Entry(root, width=45, borderwidth=5)
a.grid(row=0, column=0, columnspan=5, padx=10, pady=10) 

#Operations Buttons 

def Button_Click(Number):
    Current = a.get()
    a.delete(0, END)
    a.insert(0, str(Current) + str (Number))
def Button_Clear():
    a.delete(0, END)
def Button_Add():
    First_Number = a.get()
    global First_Num
    global math 
    math = "Addition"
    First_Num = int(First_Number)
    a.delete(0, END)
def Button_Subtract():
    FirstNumber = a.get()
    global First_Num
    global math  
    math = "Subtraction"
    First_Num = int(FirstNumber)
    a.delete(0, END)
def Button_Divide():
    First_Number = a.get()
    global First_Num
    global math
    math = "Division"
    First_Num = int(First_Number)
    a.delete(0, END)
def Button_Multiply():
    First_Number = a.get()
    global First_Num
    global math
    math = "Multiplication"
    First_Num = int(First_Number)
    a.delete(0, END)
def Button_Equal():
    Second_Number = a.get()
    a.delete(0, END)
    if math == "Addition":
        a.insert(0, First_Num + int(Second_Number))
    if math == "Subtraction":
        a.insert(0, First_Num - int(Second_Number))
    if math == "Multiplication":
        a.insert(0, First_Num * int(Second_Number))
    if math == "Division":    
        a.insert(0, First_Num // int(Second_Number))

# Listing Of Buttons 
# Passing Of Parameters In Buttons Are Done By Using lambda
Button_1 = Button(root, text="1", padx=20, pady=20, command = lambda : Button_Click(1))
Button_2 = Button(root, text="2", padx=20, pady=20, command = lambda : Button_Click(2))
Button_3 = Button(root, text="3", padx=20, pady=20, command = lambda : Button_Click(3))  
Button_4 = Button(root, text="4", padx=20, pady=20, command = lambda : Button_Click(4))
Button_5 = Button(root, text="5", padx=20, pady=20, command = lambda : Button_Click(5))
Button_6 = Button(root, text="6", padx=20, pady=20, command = lambda : Button_Click(6))
Button_7 = Button(root, text="7", padx=20, pady=20, command = lambda : Button_Click(7))
Button_8 = Button(root, text="8", padx=20, pady=20, command = lambda : Button_Click(8))
Button_9 = Button(root, text="9", padx=20, pady=20, command = lambda : Button_Click(9)) 
Button_0 = Button(root, text="0", padx=20, pady=20, command = lambda : Button_Click(0))
Button_Percentage = Button(root, text="%", padx=20, pady=20, command = lambda: Button_Click())
Button_Dot = Button(root, text=".", padx=20, pady=20, command = lambda : Button_Click())
Button_Add = Button(root, text="+", padx=20, pady=20, command =  Button_Add)
Button_Subtract = Button(root, text="-", padx=20, pady=20, command = Button_Subtract)
Button_Multiply = Button(root, text="*", padx=20, pady=20, command = Button_Multiply)
Button_Divide = Button(root, text="/", padx=20, pady=20, command = Button_Divide)
Button_Clear = Button(root, text="C", padx=20, pady=20, command = Button_Clear) # Dosent Need To Be Lambdad
Button_Delete = Button(root, text="dl", padx=20, pady=20, command = lambda : Button_Click())
Button_Equal = Button(root, text="=", padx=20, pady=53, command = Button_Equal)

# Positioning Of  Buttons In Grid System 
Button_1.grid(row=1, column=0)
Button_2.grid(row=1, column=1)
Button_3.grid(row=1, column=2)
Button_Add.grid(row=1, column=3)
Button_Clear.grid(row=1, column=4)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_Subtract.grid(row=2, column=3)
Button_Delete.grid(row=2,column=4)

Button_7.grid(row=3, column=0)
Button_8.grid(row=3, column=1)
Button_9.grid(row=3, column=2)
Button_Multiply.grid(row=3, column=3)
Button_Equal.grid(row=3, rowspan=2, column=4)

Button_0.grid(row=4, column=1)
Button_Percentage.grid(row=4, column=0)
Button_Dot.grid(row=4, column=2)
Button_Divide.grid(row=4, column=3)

root.mainloop()
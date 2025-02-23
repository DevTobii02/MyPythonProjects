#Item
#Item Price 
#Quantity 
#Totals 
print("Welcome To My Store")  

Item = input("Enter What Item Do You Want To Buy ? : ")
ItemPrice = float(input("How Much Does This Item Cost ? : "))
Quantity = int(input("How Many Will You Be Buying ? : "))
ItemsBought = print("You Bought The Following Items :  " , Quantity , Item)
Totals = Quantity * ItemPrice
print(f"Your Total Is :  {Totals:.2f}")
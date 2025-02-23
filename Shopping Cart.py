#Use Of Lists Which Allows Us To Append and Are Ordered
Foods = []
Drinks = []
FoodsPrices = []
DrinksPrices = []   
Total = 0    

while True:
    Food = input("What Food Would You Like To Get (Press q to quit ) ? : ") 
    if Food.lower() .strip() == "q":
        break # To Exit Out Of The Loop 
    else:
        FoodsPrice = float(input(f"Enter Price Of Food {Food} : $" ))
        Foods.append(Food)
        FoodsPrices.append(FoodsPrice)  
        
while True:
    Drink = input("What Drink Will You Be Getting Alongside (Press q to quit ) ? : ") 
    if Drink .lower() .strip() == "q":
        break 
    else:
        DrinksPrice = float(input("Enter The Price Of Your Drink : $"))
        Drinks.append(Drink)
        DrinksPrices.append(DrinksPrice)   
        
print("Shopping Cart".center(20, "=")) 
for Food in Foods:
    print(Food)
for FoodPrice in FoodsPrices:
    print(FoodPrice)   
for Drink in Drinks:
    print(Drink)    
for FoodPrice in FoodsPrices:
    print(FoodPrice)
for DrinkPrice in DrinksPrices:
    print(DrinkPrice) 
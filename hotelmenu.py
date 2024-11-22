#define the menu of restarurant

menu = {
    'Pizza': 180,
    'Pasta': 50,
    'Burger' : 150,
    'Salad' : 70,
    'Coffee' : 25,

}

#Greeting Customer
print('Welcome to Our Hotel')
print("Pizza: 40\nPasta:50\nBurger:150\nSalad:70\nCoffee:25")

order_total = 0

item_1 = input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added !")
else:
    print("Plse order something in the menu") 
an_order = input("Do you need any other : ")
if an_order=="yes":
    item_2 =input("Enter the name of second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print("Successfully Added Item")    
    else:
        print("It is not available")

print(f"The Total amount is :{order_total}")        

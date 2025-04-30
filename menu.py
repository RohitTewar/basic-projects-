# This program simulates a simple restaurant menu ordering system.
menu={
    'pizza': 170,
    'burger': 120,
    'sandwich': 80,
    'pasta': 150,
    'salad': 60,
    'coffee':60,

}
#greet the customer
print("Welcome to the restaurant!")
print("pizza: 170\nburger: 120\nsandwich: 80\npasta: 150\nsalad: 60\ncoffee:60")
order_total = 0
#take order from the customer

item_1 = input("Enter the first item you want to order: ")      
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Added {item_1} to your order. Total so far: {order_total}")
else:
    print(f"Sorry, we don't have {item_1} on the menu.")
    
#ask if the customer wants to order another item
another_order = input("Do you want to order another item? (yes/no): ")  
if another_order == "yes":
    item_2 = input("Enter the second item you want to order: ")  
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Added {item_2} to your order. ")
    else:
        print(f"Sorry, we don't have {item_2} on the menu.")

print(f"Your total order amount is: {order_total}")
#calculate the total amount
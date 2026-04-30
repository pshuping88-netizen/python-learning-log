#Grocery System v1

#List to hold items
grocery_list = []

#control
x = "1"

#main loop
while x == "1":
    x = input("Enter 1 to continue or 0 to exit: \n")
    if x != "1":
        break
    else:
        grocery_item = {"Item Name":input("Enter item Name: "),"Price":input("Enter item Price: "),"Quantity":input("Enter item Quantity: "),"Date":input("Enter today's date (DD/MM/YY): "),"Category":input("Enter item Category: "),"Store":input("Enter store Name: ")}
        grocery_list.append(grocery_item)

print(grocery_list)

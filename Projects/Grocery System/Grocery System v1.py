#Grocery System v1
#import module
import json

#Try to open file if not found, creates new list
try:
    with open("grocery_data.json","r") as file:
        grocery_list = json.load(file)
except FileNotFoundError:
    grocery_list = []


#control
x = "1"

#main loop
while x == "1":
    x = input("Enter 1 to continue or 0 to exit: \n")
    if x != "1":
        break
    else:
        grocery_item = {"Item Name":input("Enter item Name: "),"Price":float(input("Enter item Price: ")),"Quantity":int(input("Enter item Quantity: ")),"Date":input("Enter today's date (DD/MM/YY): "),"Category":input("Enter item Category: "),"Store":input("Enter store Name: ")}
        grocery_list.append(grocery_item)

with open("grocery_data.json", "w") as file:
    json.dump(grocery_list, file, indent=4)
    
print("Data saved successfully.")
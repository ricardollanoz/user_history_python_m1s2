from add_product import add_productt
from menu import menu
#what action the costumer wants to choose
inventory =[]
options = ["Add product","Show inventory","Calculate Statistics","Exit"]
status = "yes"

print("Select the option to run:")
menu(options)

choise= int(input("Costumer chooses option: "))

if options[choise-1] == "Add product":
    
    add_productt(inventory)
    while status == "yes":
        status = input("Do you want to register another product? (yes/no): ")
        while True:
            if status == "yes":
                add_productt(inventory)

        
        
    
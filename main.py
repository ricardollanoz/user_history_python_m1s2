from add_product import add_product
from menu import menu
from show_inventory import show_inventory
from operations import calculate_quantity, calculate_inventory
#what action the costumer wants to choose
inventory =[]
options = ["Add product","Show inventory","Calculate Statistics","Exit"]
status = "yes"
validation = True
while validation:
    choise = menu(options)
    if choise < 1 or choise > 4:
         print("ERROR! Only enter the options below")

    elif options[choise-1] == "Add product":
        status = "yes"
        while status == "yes":
            
                add_product(inventory)
                
                status = input("Do you want to register another product? (yes/no): ")
                while status not in["yes", "no"]:
                    print("ERROR! Only enter yes/no to continue")
                    status = input("Do you want to register another product? (yes/no): ")
                                          
    elif options[choise-1] == "Show inventory":
        if not inventory:
            print("Inventory is empty")
            
        else:
            show_inventory(inventory)
    
    elif  options[choise-1] == "Calculate Statistics":
        total_inventory= calculate_inventory(inventory )
        recording_products= calculate_quantity(inventory)
        print(total_inventory)
        print(recording_products)
    
    else:
        print("Muchas gracias por usar nuestros servicios")
        validation = False

                
    
            




        
        
    
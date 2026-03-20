def calculate_inventory(inventory):
    total_inventory = 0
   
    for index in inventory:
        total_inventory += index['price'] * index['quantity']
       
    return total_inventory

def calculate_quantity(inventory):   
       
    recording_products = len(inventory)
    return recording_products
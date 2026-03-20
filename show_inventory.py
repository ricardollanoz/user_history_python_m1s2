def show_inventory(inventory):
    for detail in inventory:
                print(f"Producto: {detail['name']}")
                print(f"Price {detail['price']}")
                print(f"Quantity: {detail['quantity']}\n")
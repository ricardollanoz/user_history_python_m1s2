#function to add product unlimited times until the costumer finishes

def add_product(inventory):
    
    product_name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = {
        'name': product_name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    
        



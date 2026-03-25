from validations import valid_not_empty_text, valid_positive_number
#function to add product unlimited times until the costumer finishes

def add_product(inventory):
    
    product_name = valid_not_empty_text("Name product: ")
    price = valid_positive_number("Price: ")
    quantity = valid_positive_number("Quantity: ")

    product = {
        'name': product_name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    
        



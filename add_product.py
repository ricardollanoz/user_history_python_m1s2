#function to add product unlimited times until the costumer finishes
inventory=[]
def add_productt(inventory):
    count=0
    while True:
        
        for i in range(count):
            print(f"Produc registration #{i+1}")
        
            

            product_name = input("Product name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            product = {
                'name': product_name,
                'price': price,
                'quantity': quantity
            }
            inventory.append(product)
        count += 1
add_productt(inventory)


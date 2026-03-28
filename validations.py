def valid_not_empty_text(message):
    validate = True
    while validate:
        text = input(message).strip()
        
        # .replace(" ", "") allows for multi-word names like "Red Apple"
        if text.replace(" ", "").isalpha():
            validate = False
        
        else:
             print("ERROR! Name must only contain letters")
    return text

#This function is used to verify that a number cannot be negative
def valid_positive_number(message):
    validate = True
    while validate:
        try:
            data = int(input(message).strip())
            if  data <= 0:
                 print("\n The value cannot be negative")
            else:
                 validate=False 
                 return data

        except ValueError:
                print("\n The input is invalid")


        
    


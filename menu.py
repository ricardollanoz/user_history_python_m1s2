def menu(options):
    print("Select the option to run:")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    choise= int(input("Costumer chooses option: "))
    return choise
inventory = {}
prices = {}
while True:
    print("******************CHOICE*************************")
    print("""
    1. Add an article
    2. Remove an article
    3. Show stock
    4. Exit
    """)
    print("******************-------*************************")

    choice = input("What would you like to do? ")
    
    if choice == "1":
        name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price = float(input("Enter the price per unit: "))
        
        if name in inventory:
            inventory[name] += quantity
            prices[name] += price
            print("Product updated")
        else:
            inventory[name] = quantity
            prices[name] = price
            print("Product added")
            
    elif choice == "2":
        name = input("Enter the product name to remove: ")
        
        if name in inventory:
            inventory.pop(name)
            prices.pop(name)
            print("Product removed")
        else:
            print("Product not found")
            
    elif choice == "3":
        stock = 0
        
        for name in inventory:
            print("Product name: {}, Quantity: {}, Price per unit: {}".format(name, inventory[name], prices[name]))
            stock += inventory[name]
        
        print("Total stock: {}".format(stock))
        
    elif choice == "4":
        print("See you later!")
        break
        
    else:
        print("Invalid choice. Try again.")

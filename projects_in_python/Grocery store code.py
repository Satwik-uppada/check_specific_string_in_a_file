inventory = dict()

try:
    def activites():
        print("list of activities:")
        print("1.Add an item")
        print("2.Remove an item")
        print("3.Update the item")
        print("4.Display the inventory")
        activity = int(input("Select your option: "))
        return activity
except:
    print("This function is facing ")

try:
    def details():
        name = input("Enter the name of the item:")
        quantity = int(input("Enter the quantity of the item: "))
        price = int(input("Enter the price of the item:"))
        return name, quantity, price
except:
    print("This function is facing ")

try:
    def add_item(name, quantity, price):
        inventory[name] = {}
        inventory[name]['quantity'] = quantity
        inventory[name]['price'] = price
except:
    print("This function is facing ")

try:
    def remove_item(inventory):
        name = input("Which item you want to remove:")
        if name in inventory:
            del inventory[name]
        else:
            print("Item not found")
except:
    print("This function has an error")

try:
    def update_value(name):
        print("Which field do you want to change??: ")
        print("1.Price")
        print("2.Quantity")
        print("3.Both")
        print("Feel free to change anything.... :)")
        change = int(input("Select one option: "))

        if change == 1:
            MRP = float(input("Enter new price=pr: "))
            inventory[name]['price'] = MRP
        elif change == 2:
            quantity = float(input("Enter new quantity: "))
            inventory[name][quantity] = quantity
        elif change == 3:
            quantity = float(input("Enter new quantity: "))
            MRP = float(input("Enter new price: "))
            inventory[name][quantity] = quantity
            inventory[name]['price'] = MRP
        else:
            print("oh hoo please choose in given options.... ")
            update_value(name)

except:
    print("This function has an error")

try:
    def view_inventory(inventory):
        print('Inventory')
        for item, details in inventory.items():
            print(f"{item}:{details}")
            print("Thanks for shopping")
except:
    print("This function has an error")

name, quantity, price = details()
add_item(name, quantity, price)
activity = activites()
if activity == 1:
    details()
    add_item(name, quantity, price)

elif activity == 2:
    remove_item(inventory)

elif activity == 3:
    update_value(name)

elif activity == 4:
    view_inventory(inventory)
else:
    print("please select correct option.")
    activites()

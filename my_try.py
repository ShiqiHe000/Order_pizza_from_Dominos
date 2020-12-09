from pizzapy import Customer, StoreLocator, Order

# search menu 
def searchMenu(menu):
    print("\nYou are now searching the menu...")

    item = input("Type an item to look for" 
                 " (press Enter if you want to stop)\n").strip().lower()

    if len(item) > 1:
        item = item[0].upper() + item[1:]
        print(f"\nResults for: {item}\n")
        menu.search(Name = item)
    else:
        print("No Results")

def addToOrder(order):
    print("\nPlease type in the code of the item you's like to order...")
    print("Press ENTER to stop ordering.\n")
    while True:
        item = input("Code: ").strip().upper()
        try:
            order.add_item(item)
        except:
            if item == "":
                break
            print("Invalid code, try again. ")

# print the customer's order
def printOrder(order):
    print(order)
    price = 0
    if order.data['Products']:
        for item in order.data['Products']:
            price += float(item['Price'])
            print(item['Name'] + " $" +item['Price'])
    print("\nYour order total is: $" + str(price) + " + TAX.")

# allows the customer to remove the selected order
def removeOrder(order):
    print("\nDo you want to remove any order?")
    wantToRemove = input("(y/n): ")
    if wantToRemove in ['Yes', 'y']:
        pass


# customer info
customer = Customer("Shiqi", "He", "example@gmail.com", \
                    "1234567890", "75 Laurier Ave. E, Ottawa, ON, K1N 6N5")

# find the dominos
my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print("Your closest Domino: \n" + str(my_local_dominos))

#print("\nHere is the menu: \n")

# find menu
menu = my_local_dominos.get_menu()
order = Order.begin_customer_order(customer, my_local_dominos, 'ca')

# let the customer set the order
while True:
    searchMenu(menu)
    addToOrder(order)
    answer = input("Would you like to add more item (y/n) ?").lower()
    if answer not in ['yes', 'y']:
        break 

print("\nYour order is as follows:\n")
printOrder(order)
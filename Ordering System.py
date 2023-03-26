# Define the menu items and their prices
menu = {
    "Burger": 5.99,
    "Fries": 2.99,
    "Soda": 1.99
}

# Define a function to display the menu
def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

# Define a function to take the user's order
def take_order():
    order = {}
    while True:
        item = input("What would you like to order? ").title()
        if item not in menu:
            print("Sorry, that item is not on the menu.")
        else:
            quantity = int(input("How many would you like? "))
            order[item] = quantity
            again = input("Would you like to order anything else? (y/n) ")
            if again.lower() == "n":
                break
    return order

# Define a function to calculate the total cost of the order
def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        price = menu[item]
        total += price * quantity
    return total

# Display the menu and take the user's order
display_menu()
order = take_order()

# Calculate the total cost of the order and display it to the user
total = calculate_total(order)
print(f"Your total is ${total:.2f}. Thank you for your order!")

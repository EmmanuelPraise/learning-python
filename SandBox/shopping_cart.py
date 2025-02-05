menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []  # List to store selected items
order = {}  # Dictionary to store ordered items with quantity and total price
total = 0  # Total cost of all ordered items
menu_items = list(menu.keys())  # List of item names for easier lookup

# Display the menu
print(f"{'-' * 7} MENU {'-' * 7}")
print("SN ITEM        PRICE")
for sn, (item, price) in enumerate(menu.items(), start=1):
    print(f"{sn}. {item:10}: ${price:.2f}")
print("-" * 20)

# Shopping process loop
while True:
    item_input = input("Select an item by name or serial number (Q to quit): ").lower()

    if item_input == "q":  # Exit condition
        break

    # Try to convert input to integer (for selecting by serial number)
    try:
        item_index = int(item_input) - 1
        if 0 <= item_index < len(menu_items):
            item = menu_items[item_index]
        else:
            print("Invalid serial number. Please try again.")
            continue
    except ValueError:
        item = item_input  # Assume input is an item name

    if item not in menu:  # Validate item selection
        print("Invalid item. Please select from the menu.")
        continue


    try:
        item_quantity = int(input("Enter quantity: "))
        if item_quantity <= 0:
            print("Quantity must be at least 1. Please try again.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a valid number.")
        continue


    item_total_price = menu[item] * item_quantity
    if item in order:
        order[item]["quantity"] += item_quantity
        order[item]["total_price"] += item_total_price
    else:
        order[item] = {"quantity": item_quantity, "total_price": item_total_price}

    total += item_total_price  # Update the total cost

# Display invoice
print(f"{'-' * 6} INVOICE {'-' * 5}")
print("SN ITEM        QUANTITY   PRICE")
for sn, (item, details) in enumerate(order.items(), start=1):
    print(f"{sn}. {item:10} {details['quantity']:8} ${details['total_price']:.2f}")

print(f"Total: ${total:.2f}")

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

cart = []
order = {}
total = 0

print(f"{'-' * 7} MENU {'-' * 7}")
print("SN ITEM        PRICE")
for sn, (item, price) in enumerate(menu.items(), start=1):
    print(f"{sn}. {item:10}: ${price:.2f}")
print("-" * 20)

while True:
    item = input("Select an item (Q to quit): ").lower()
    if item == "q":
        break
    if item not in menu:
        print("Invalid item. Please select from the menu.")
        continue

    try:
        item_quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    if item in order:
        order[item]["quantity"] += item_quantity
        order[item]["total_price"] += menu[item] * item_quantity
    else:
        order[item] = {"quantity": item_quantity, "total_price": menu[item] * item_quantity}

    total += menu[item] * item_quantity  # Accumulate the total price

print(f"{'-'*6} INVOICE {'-'*5}")
print("SN ITEM        QUANTITY PRICE")
for sn, (item, details) in enumerate(order.items(), start=1):
    print(f"{sn}. {item:10} {details['quantity']:8} ${details['total_price']:.2f}")

print(f"Total: ${total:.2f}")

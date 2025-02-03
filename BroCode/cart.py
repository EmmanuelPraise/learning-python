# Shopping cart program
items_list = []
prices  = []
total = 0

while True:
    item = input("Enter a item to buy (Q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {item}: $"))
        items_list.append(item)
        prices.append(price)

print()
print(f"{"-" * 5} CART {"-" * 5}")

for index, items in enumerate(zip(items_list, prices), start=1):
    item, price = items
    print(f"{index}. {item} = ${price}")
    total += price
print(f"Total: ${total:.2f}")
print("-" * 16)

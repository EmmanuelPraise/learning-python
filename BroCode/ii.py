
# Nested Loop  =  A loop within another loop (outer, inner)
# It can contain while loops and for loops
# outer loop:
#    inner loop:

# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print()
#
#
# symbol = "*"
# row_num = 4
# column_num = 5
# for row in range(row_num):
#     for x in symbol * column_num:
#         print(x, end="")
#     print()
#
# # Triangle format
# row = 3
# column_num = 4
# symbol = "+"
# for row in range(1,column_num):
#     for x in symbol * row:
#         print(x, end="")
#     print()

# Collection  = single "Variable" used to store multiple variables
# Examples = List, Set, Tuple, Dictionary

# List
# fruits = ["Apple", "Orange", "Banana", "Coconut"]
# print(dir(fruits))  # To see the list of methods that can be performed on a variable
# print(help(fruits))  # To see more about a variable
# print(len(fruits))
# print("Apple" in fruits)

# # Set
# fruits = {"Apple", "Orange", "Banana", "Coconut"}
# print(dir(fruits))  # To see the list of methods that can be performed on a variable
# print(help(fruits))  # To see more about a variable
#
# # Tuple
# fruits = ("Apple", "Orange", "Banana", "Coconut")
# print(dir(fruits))  # To see the list of methods that can be performed on a variable
# print(help(fruits))  # To see more about a variable

# # Shopping cart program
# items_list = []
# prices  = []
# total = 0
#
# while True:
#     item = input("Enter a item to buy (Q to quit): ")
#     if item.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of {item}: $"))
#         items_list.append(item)
#         prices.append(price)
#
# print()
# print(f"{"-" * 5} CART {"-" * 5}")
#
# for index, items in enumerate(zip(items_list, prices), start=1):
#     item, price = items
#     print(f"{index}. {item} = ${price}")
#     total += price
# print(f"Total: ${round(total,2)}")
# print("-" * 16)

# 2D List
# groceries = [["apple", "banana", "coconut"], ["yam", "rice", "potato"], ["Fish", "Chicken", "Beef"]]
# print(groceries)
# print(groceries[0][0])
# for row in groceries:
#     for item in row:
#         print(item, end=" ")
#     print()

# dail_pad = ((1,2,3), (4,5,6), (7,8,9), ("*",0,"#"))
#
# for row in dail_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

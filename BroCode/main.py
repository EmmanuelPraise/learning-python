
import sys
import random
import math

# print("Hello world!")
# print("My first python program")
# print(sys.version)

x,y,z = "yaman", "ali", "mohammed"
# print(x)
# print(y)
# print(z)

x=y=z="yaman"
# print(x)
# print(y)
# print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)


colors = ["red", "blue", "green", "yellow", "black", "white", "orange", "purple", "pink", "brown"]
# print(random.choice(colors))
random.shuffle(colors)
# print(colors)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
splitter= text.split(" ")
word_count = len(splitter)
char_count = len(text)
# print(f"{word_count} Words, {char_count} Characters")
#
# print(text.index("o"))

# # Area of a Rectangle
# length = float(input("Enter the Length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"Area = {area}cm^2")
#
# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity
# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: ${total}")

# # Mad-libs Game
# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")
#
# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}")

# Circumference of a circle
# radius = float(input("Enter a radius: "))
# pi = math.pi
# circumference = 2*pi*radius
# print(f"circumference = {circumference:.2f}")

# Area of a circle
# area = pi*pow(radius, 2)
# print(f"Area = {round(area, 2)}cm^2")

# Program to find the hypotenuse of a right angle triangle
# adj = float(input("Enter the Adjacent: "))
# opp = float(input("Enter the opposite: "))
# hyp = round(math.sqrt(pow(adj, 2) + pow(opp, 2)), 2)
# print(f"Hypotenuse of the Triangle = {hyp}")

# name = input("What is your name? ")
# if name:
#     print(f"Hello {name}!")
# else:
#     print("You didn't type your name!")

# age =  int(input("Enter Your Age: "))
# if age >= 18:
#     print("You are now signed up!")
# else:
#     print("You  must be 18+ to sign up")


list_items = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
list_items[1:2] = ["blackcurrant", "watermelon", "grape", "banana"]
list_items.insert(1,"papaya")
# print(list_items)

# Nested Loop  =  A loop within another loop (outer, inner)
# It can contain while loops and for loops
# outer loop:
#    inner loop:

# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print()


symbol = "*"
row_num = 4
column_num = 5
# for row in range(row_num):
#     for x in symbol * column_num:
#         print(x, end="")
#     print()

# Triangle format
row = 3
column_num = 4
symbol = "+"
# for row in range(1,column_num):
#     for x in symbol * row:
#         print(x, end="")
#     print()

# Collection  = single "Variable" used to store multiple variables
# Examples = List, Set, Tuple, Dictionary

# List
fruits = ["Apple", "Orange", "Banana", "Coconut"]
# print(dir(fruits))  # To see the list of methods that can be performed on a variable
# print(help(fruits))  # To see more about a variable
# print(len(fruits))
# print("Apple" in fruits)

# 2D List
groceries = [["apple", "banana", "coconut"], ["yam", "rice", "potato"], ["Fish", "Chicken", "Beef"]]
# print(groceries)
# print(groceries[0][0])
# for row in groceries:
#     for item in row:
#         print(item, end=" ")
#     print()

dail_pad = ((1,2,3), (4,5,6), (7,8,9), ("*",0,"#"))

# for row in dail_pad:
#     for num in row:
#         print(num, end=" ")
#     print()

# Set
fruits = {"Apple", "Orange", "Banana", "Coconut"}
# print(dir(fruits))  # To see the list of methods that can be performed on a variable
# print(help(fruits))  # To see more about a variable

# Tuple
# fruits = ("Apple", "Orange", "Banana", "Coconut")
# print(dir(fruits))  # To see the list of methods that can be performed on a variable
# print(help(fruits))  # To see more about a variable

# Dictionary

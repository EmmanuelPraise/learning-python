# import sys


# print("Hello world!")
# print("My first python program")
# print(sys.version)

# x,y,z = "yaman", "ali", "mohammed"
# print(x)
# print(y)
# print(z)
#
# x=y=z="yaman"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)

# import random
#
# colors = ["red", "blue", "green", "yellow", "black", "white", "orange", "purple", "pink", "brown"]
# print(random.choice(colors))
# random.shuffle(colors)
# print(colors)

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
# splitter= text.split(" ")
# word_count = len(splitter)
# char_count = len(text)
# print(f"{word_count} Words, {char_count} Characters")

# print(text.index("o"))

# Area of a Rectangle
# length = float(input("Enter the Length: "))
# width = float(input("Enter the width: "))
# area = length * width
# print(f"Area = {area}cm^2")

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

# import math
# # Circumference of a circle
# radius = float(input("Enter a radius: "))
# pi = math.pi
# circumference = 2*pi*radius
# print(f"circumference = {round(circumference, 2)}")
#
# # Area of a circle
# area = pi*pow(radius, 2)
# print(f"Area = {round(area, 2)}cm^2")

# Program to find the hypotenuse of a right angle triangle
# adj = float(input("Enter the Adjacent: "))
# opp = float(input("Enter the opposite: "))
# hyp = round(math.sqrt(pow(adj, 2) + pow(opp, 2)), 2)
# print(f"Hypotenuse of the Triangle = {hyp}")

# age =  int(input("Enter Your Age: "))
#
# if age >= 18:
#     print("You are now signed up!")
# else:
#     print("You  must be 18+ to sign up")


# name = input("What is your name? ")
#
# if name:
#     print(f"Hello {name}!")
# else:
#     print("You didn't type your name!")

# # Unit converter
# weight = float(input("Enter Weight: "))
# unit = input("Kilograms or Pounds? (K or L): ").upper()
#
# if unit == "K":
#     weight *= 2.205
#     unit = "Lbs."
#     print(f"Your weight is: {round(weight, 2)}{unit}")
# elif unit == "L":
#     weight /= 2.205
#     unit = "Kgs."
#     print(f"Your weight is: {round(weight, 2)}{unit}")
# else:
#     print(f"{unit} was not valid.")


# # Temperature converting program
#
# unit = input("Enter Temperature unit (F or C): ").upper()
# temp = float(input("Enter Temperature Value: "))
#
# if unit == "C":
#     temp = (9 * temp) / 5 + 32
#     unit = "°F."
#     print(f"Temperature: {round(temp, 2)}{unit}")
# elif unit == "F":
#     temp = (temp - 32) * 5/9
#     unit = "°C."
#     print(f"Temperature: {round(temp, 2)}{unit}")
# else:
#     print("Invalid input!")

# list_items = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# list_items[1:2] = ["blackcurrant", "watermelon", "grape", "banana"]
# list_items.insert(1,"papaya")
# print(list_items)

# principal = 0
# interest_rate = 0
# time = 0
#
# while principal <= 0:
#     principal = float(input("Enter the principal amount: "))
#     if principal <= 0:
#         print("Principal can't be less than or equal to zero!")
#
# while interest_rate <= 0:
#     interest_rate = float(input("Enter the interest_rate amount: "))
#     if interest_rate <= 0:
#         print("Interest interest_rate can't be less than or equal to zero!")
#
# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("time can't be less than or equal to zero!")
#
# total_amount = principal * pow((1 + interest_rate/100), time)
# print(f"Balance after {time} year/s: ${total_amount:.2f}")
# print(principal); print(interest_rate); print(time)

# import time
# import random
#
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time):
#     print(x)
#     time.sleep(1)
# print("TIME'S UP!")
#
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)
# print("TIME'S UP!")
#
# # Countdown timer
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time, 0, -1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME'S UP!")
#
# # Count-up timer
# my_time = int(input("Enter the time in seconds: "))
# for x in range(my_time):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME'S UP!")
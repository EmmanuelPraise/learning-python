
# 1. Variables and Data Types:
# Write a program to store your name, age, and favorite color in variables, then print them.
name = "Emmanuel"
age = 19
favorite_color = "Sky Blue"

print(name)
print(age)
print(favorite_color)

# Calculate the area of a rectangle using length and width stored in variables.
length = 5.3453
breadth = 7.454
rectangle_area = float(round(length * breadth, 2))
print(rectangle_area)

# 2. Conditions:
# Write a program that checks if a number is even or odd.
num = 5

if num % 2 == 0:
    print(f"{num} is an Even number.")
elif num % 2 != 0:
    print(f"{num} is an Odd number.")
else:
    print("Invalid Input!, input a number.")

# Create a simple grading system where a score determines the grade (e.g., A, B, C).
score = 75
grade = ""
if 70 <= score <= 100:
    grade = "A"
elif 70 > score >= 60:
    grade = "B"
elif 60 > score >= 50:
    grade = "C"
elif 50 > score >= 40:
    grade = "D"
elif 40 > score >= 30:
    grade = "E"
elif 30 > score >= 0:
    grade = "F"
print(f"Result: Score = {score}, Grade = {grade}.")

# 3. Loops:
# Print all numbers from 1 to 50 using a for loop.
number_range = 50
for i in range(1,number_range + 1):
    print(i, end=",")

# Use a while loop to let the user guess a predefined number until they get it right.
number = 5
while True:
    print("Guess a Number between 1-10.")
    guess = int(input("Guess: "))
    if guess > number:
        print("Guess too high, Try again!")
    elif guess < number:
        print("Guess too low, Try again!")
    elif number == guess:
        print("Correct!")
        break
    else:
        print("Invalid Input!, input a number.")

# 4. Lists and Arrays:
# Create a list of five favorite fruits and print each fruit using a loop.
favorite_fruits = ["Apple", "Mango", "Orange", "Paw-Paw", "Cherry", "Grape"]
for fruit in favorite_fruits:
    print(fruit)

# Add a fruit to the list and sort it alphabetically.
new_fruit = favorite_fruits.append("Blueberry")
favorite_fruits.sort()
print(favorite_fruits)

# 5. Dictionaries:
# Create a dictionary with three key-value pairs (e.g., name, age, city) and print each value.
person = {
    "name": "Emmanuel",
    "age": 19,
    "city": "New-York"
}

for i in person.values():
    print(i)

# Update a value in the dictionary and display the updated dictionary.
person["name"]= "Abel"
print(person)

# 6. Functions:
# Write a function to calculate the square of a number.
def square(number):
    return number**2

print(square(10))

# Create a function that takes two numbers and returns their sum.
def add(first_number = 0, second_number = 0):
    return first_number + second_number

print(add(2,2))

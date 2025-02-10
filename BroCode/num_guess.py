import random

low = 1
high = 10

number = random.randint(low,high)
guesses = 2
print(number)

while True:
    guess = int(input(f"Guess a number between {low}-{high}: "))
    if guesses == 0:
        print("Guess Limit Reached!")
        break
    elif guess < low or guess > high:
        print(f"{guess} is out of range, Try again!")
        print(f"{guesses} Guess(es) Left!")
    elif guess > number :
        print("Guess too High, Try again!")
        print(f"{guesses} Guess(es) Left!")
    elif guess < number:
        print("Guess too Low, Try again!")
        print(f"{guesses} Guess(es) Left!")
    elif guess == number:
        print(f"{number} is the correct guess.")
        # print(f"{guesses} Guess(es) Left!")
        break
    guesses -= 1

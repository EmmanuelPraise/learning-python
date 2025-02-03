
# Timer Program
import time

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time):
    print(x)
    time.sleep(1)
print("TIME'S UP!")

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)
print("TIME'S UP!")

# Countdown timer
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!")

# Count-up timer
my_time = int(input("Enter the time in seconds: "))
for x in range(my_time):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!")

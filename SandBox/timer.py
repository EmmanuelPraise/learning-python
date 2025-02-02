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
#
#
# def pause_timer(duration):
#     for x in range(duration):
#         seconds = x % 60
#         minutes = int(x / 60) % 60
#         hours = int(x / 3600)
#         print(f"{hours:02}:{minutes:02}:{seconds:02}")
#         time.sleep(1)
#         if x == duration // 2:  # Pause at halfway point for demonstration
#             input("Timer paused. Press Enter to continue...")
#
#     print("TIME'S UP!")
#
# # Example usage
# pause_timer(10)
#
#
# def pause_timer(duration):
#     pause_point = random.randint(0, duration - 1)
#     for x in range(duration):
#         seconds = x % 60
#         minutes = int(x / 60) % 60
#         hours = int(x / 3600)
#         print(f"{hours:02}:{minutes:02}:{seconds:02}")
#         time.sleep(1)
#         if x == pause_point:
#             user_input = input("Type 'pause' to pause the timer: ")
#             if user_input.lower() == 'pause':
#                 input("Timer paused. Press Enter to continue...")
#
#     print("TIME'S UP!")
#
# # Example usage
# pause_timer(10)
#
# def pause_timer(duration):
#     for x in range(duration):
#         seconds = x % 60
#         minutes = int(x / 60) % 60
#         hours = int(x / 3600)
#         print(f"{hours:02}:{minutes:02}:{seconds:02}")
#         time.sleep(1)
#         if input() == '':
#             input("Timer paused. Press Enter to continue...")
#
#     print("TIME'S UP!")
#
# # Example usage
# pause_timer(10)

students = [
    {
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science",
        "grades": {"math": 90, "science": 85, "english": 88}
    },
    {
        "name": "Jane Smith",
        "age": 22,
        "major": "Mathematics",
        "grades": {"math": 95, "science": 80, "english": 82}
    },
    {
        "name": "Emily Johnson",
        "age": 21,
        "major": "Physics",
        "grades": {"math": 85, "science": 90, "english": 87}
    },
    {
        "name": "Michael Brown",
        "age": 23,
        "major": "Chemistry",
        "grades": {"math": 80, "science": 88, "english": 84}
    }
]

# for student in students:
#     first_name, last_name = student['name'].split(" ")
#
#     print(f"Hello, {first_name}!")

my_list = ["blue", "red", "black"]
# length = []
# for item in range(len(my_list)):
#     length.append(item)
#     print(item)
# print(length)

# length = [item for item in range(len(my_list))]
# print(length)

# even_numbers = [num for num in range(1, 11) if num % 2 == 0]
# print(even_numbers)

# num = [1,1,1,1,1]
# sum_num = 0
#
# for x in num:
#     sum_num += x
# print(sum_num)

# while True:
#     username = input("Enter a Username: ")
#     if len(username) > 12:
#         print("Username can't be more than 12 characters.")
#     elif username == " ":
#         print("Username can't contain space")
#     elif username == "":
#         print("Username can't be empty")
#     elif not username.isalpha():
#         print("Username can't contain digits")
#     else:
#         print(f"Welcome, {username}!")
#         break

# i = 0
# while i <= 9:
#     print(i)
#     i += 1

# students = [
#     {
#         'firstname': 'David',
#         'lastname': 'Smith',
#         'matric_number': 20221920,
#         'department': 'accounting',
#         'email': 'davie612@outlook.com',
#         'phone': 9139268581
#     }
# ]
#
# def new_student(name, matric_number, department, email, phone):
#     first_name, last_name = name.split(" ")
#     add_student = students.append(dict(first_name=first_name, last_name=last_name, matric_number=matric_number, department=department, email=email, phone=phone))
#     return students[-1]
#
# print(new_student(fullname = "Emmanuel Ayelabola", matric_number = 20221902, department = Agricultural and Bio-Resources Engineering, email = ayelabolaeo.22@student.funaab.edu.ng, phone = 09139268581))

# def remove_student(name):
# # Searching by name
#     for student_index, student in zip(range(len(students)), students):
#         if student["name"] == name:
#             return students.pop(student_index)
#
# remove_student("John Doe")
# print(students)
# remove_student("Michael Brown")
# print(students)

# name = "Emmanuel"
# print(name[::-1])
#
# score = float(input("Enter a Score: "))
# if 70 <= score <= 100:
#     print("Grade = A")
# elif 70 > score >= 60:
#     print("Grade = B")
# elif 60 > score >= 50:
#     print("Grade = C")
# elif 50 > score >= 40:
#     print("Grade = D")
# elif 40 > score >= 30:
#     print("Grade = E")
# elif 30 > score >= 0:
#     print("Grade = F")
# elif score > 100 or score < 0:
#     print("Score doesn't exist!")
# else:
#     print("Invalid Input!")

# numbers_ent = input("Enter list of numbers: ")
# numbers_list = numbers_ent.split(" ")
#
# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter a symbol to use: ")
#
# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end=" ")
#     print()

# Unit converter
weight = float(input("Enter Weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)}{unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 2)}{unit}")
else:
    print(f"{unit} was not valid.")


# Temperature converting program
unit = input("Enter Temperature unit (F or C): ").upper()
temp = float(input("Enter Temperature Value: "))

if unit == "C":
    temp = (9 * temp) / 5 + 32
    unit = "°F."
    print(f"Temperature: {round(temp, 2)}{unit}")
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "°C."
    print(f"Temperature: {round(temp, 2)}{unit}")
else:
    print("Invalid input!")
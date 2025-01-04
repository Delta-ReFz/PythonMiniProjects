'''
if statement
'''

weight = float(input("Enter you weight: "))
unit = input("Kilograms or Pounds? (K or L): ").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight is {weight:.2f} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is {weight:.2f} {unit}")
else:
    print(f"{unit} is not valid")



unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp} degrees.")
elif unit == "F":
    temp = round(((temp - 32) * 5 ) / 9, 1)
    print(f"The temperature in Celsius is {temp} degrees.")
else:
    print("Wrong input")
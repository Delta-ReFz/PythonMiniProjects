'''
List, sets & tuples, append()
'''

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("---------- YOUR CART ----------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total = total + price

print(f"\nYour total is ${total}")
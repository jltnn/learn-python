item = input("What do you want to buy?:")
price = float(input("what is the price?:"))
quantity = int(input("how many would you like?:"))

total = price * quantity

print(f"You have bought {quantity} {item}")
print( f"Your total price is: ${total}")

import math
radius = float(input("Enter the radius"))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

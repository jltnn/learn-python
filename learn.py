import math
radius = float(input("Enter the radius"))
circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")

area = math.pi * pow(radius, 2)
print(f"The area is: {round(area, 2)}cm^2")
a = int(input("Enter the a:"))
b = int(input("Enter the b:"))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print (f"The value of c is {c}cm")

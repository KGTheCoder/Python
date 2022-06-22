import math

x = float(input("Enter point x: "))
y = float(input("Enter point y: "))
r = float(input("Enter the radius: "))

hypotenuse = math.sqrt(pow(x, 2) + pow(y,2))

if hypotenuse <= r:
    print("The point  belongs to a circle")
else:
    print("The point does not belong to a circle.")
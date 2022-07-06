# Import the math module
import math

# Ask the user for the x and y coordinates, as well as the radius 
x = float(input("Enter point x: "))
y = float(input("Enter point y: "))
r = float(input("Enter the radius: "))

# Define the hypotense equation 
hypotenuse = math.sqrt(pow(x, 2) + pow(y,2))

# If the hypotenuse is less than or equal to the radius, 
if hypotenuse <= r:

    # Print that the point belongs to the circle
    print("The point  belongs to a circle")

# Otherwise,     
else:

    # Print that it is not
    print("The point does not belong to a circle.")
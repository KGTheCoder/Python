x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
z = int(input("Please enter the third number: "))

print("The maximum number is: ", end="")
if y <= x >= z:
    print(x)
elif x <= y >= z:
    print(y)
elif x <= z >= y:
    print(z)

x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

while x != 0 and y != 0:
    if x > y:
        x %= y
    else:
        y &= x
    
GCD = x + y
print("The greatest common divisor = ", GCD)
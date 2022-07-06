x = abs(int(input("Please enter any number: ")))

factorial = 1
while x > 1:
    factorial *= x
    x -= 1
print("The result of factorial = ", factorial)
x = abs(int(input("Please enter any number: ")))

factorial = 1
for i in range(2, x + 1):
    factorial *= i

print("The result of factorial = ", factorial)
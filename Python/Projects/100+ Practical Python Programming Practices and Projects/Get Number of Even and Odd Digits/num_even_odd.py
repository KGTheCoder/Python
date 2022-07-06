x = int(input("Please enter some numbers: "))

even = 0
odd = 0

while x > 0:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
    x = x // 10

print("Even numbers = %d, Odd numbers = %d" %(even,odd))
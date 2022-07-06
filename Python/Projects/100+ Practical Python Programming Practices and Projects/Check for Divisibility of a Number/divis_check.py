x = int(input("Please enter the numerator: "))
y = int(input("Please enter the denominator: "))

if x % y == 0:
    print(x, "is divisible by", y)
else:
    print("No way!", x, "is not divisible by", y)
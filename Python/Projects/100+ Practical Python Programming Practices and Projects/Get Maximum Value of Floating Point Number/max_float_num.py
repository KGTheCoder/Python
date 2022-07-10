x = float(input("Please enter floating point numbers only: "))

y = str(x)
max = -1

for i in range(len(y)):
    if y[i] == '.':
        continue
    elif max < int(y[i]):
        max = int(y[i])

print("The maximum element is =", max)

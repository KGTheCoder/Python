import math 

x = int(input("Please enter a number to check: "))

if x < 2:
    print("Please enter a number greater than or equal to 2")
    quit()
elif x == 2:
    print("This is a prime number!")
    quit()

y = 2
num = int(math.sqrt(x))

while y <= num:
    if x % y == 0:
        print("This is not a prime number!!!")
        quit()
    y += 1
    
print("This is a prime number")

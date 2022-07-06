num1 = int(input("Please enter a number to convert: "))

x = num1

base_num = int(input("Choose a base(2 - 9): "))

if not(2 <= base_num <= 9):
    quit()

num2 = ""

while num1 > 0:
    num2 = str(num1%base_num) + num2
    num1 //= base_num
output = "The value of {} in base {} is {}"
print(output.format(x, base_num, num2))

str1 = str(input("Please enter values: "))

sum_digit = 0
pro_digit = 1
for x in str1:
    if x.isdigit() == True:
        z = int(x)
        sum_digit = sum_digit + z
        pro_digit *= z

print("Sum of digits =", sum_digit)
print("Product of digits =", pro_digit)
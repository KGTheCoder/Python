str1 = input("Please enter the starting letter: ")
str2 = input("Please enter the ending letter: ")

while str1 <= str2:
    print(str1, end = " ")
    str1 = chr(ord(str1) + 1)
print()
str = "Hi, Hello, How, Are, You"
print(str)

substr1 = input("Please choose a substring to replace: ")
substr2 = input("Please insert the new substring: ")
lensubstr1 = len(substr1)

while str.find(substr1) > 0:
    i = str.find(substr1)
    str = str[:i] + substr2 + str[i + lensubstr1:]
print(str)
print("Please enter the length of the proposed triangle: ")

x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if x + y > z and x + z > y and y + z > x:
    print("The triangle of xyz exists")
else:
    print("This triangle does not exist")
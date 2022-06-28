print("'End' terminates the program")

while True: 
    o = input("Choose an Operator(+, -, *, /): ")
    if o == "end" or o == "End":
        break
    if o in ('+', '-', '*', '/'):
        x = float(input("Enter the value of x: "))
        y = float(input("Enter the value of y: "))
        if o == '+':
            print("%.2f"%(x+y))
        elif o == '-':
            print("%.2f"%(x-y))
        elif o == '*':
            print("%.2f"%(x*y))
        elif o == "/":
            if y != 0:
                print("%.2f"%(x/y))
            else:
                print("Error! Cannot divide by zero!")
        else:
            print("Invalid operator")

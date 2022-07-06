# Variable used to produce the rows
x = 1

while x < 10:

    # Variable used to produce the columns 
    y = 1
    while y < 10:
        print("%4d"%(x*y),end="")
        y +=1 
    print()
    x+=1
# User input
x = input("Please enter any value of 'C' or 'F': ")

# Checks the last character of the input string 
unit = x[-1]

# Grab the int value of the input
x = int(x[0:-1])

# If the last character begins with 'C' or 'c,'
if unit == 'C' or unit == 'c':

    # Convert int value to Fahrenheit
    x = round(x*(9/5)+32)
    print(str(x) + ' degrees F')

# Else, if the last character begins with 'F' or 'f,'
elif unit == 'F' or unit == 'f':
    
    # Convert int value to Celsius 
    x = round((x-32)*(5/9))
    print(str(x) + ' degrees C')

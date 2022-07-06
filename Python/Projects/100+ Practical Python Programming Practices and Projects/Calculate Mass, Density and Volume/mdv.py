# Empty result value used to store our final answer
result = 0

# User input the calculate mass, density or volume
mdv = input("Please choose one to calculate(m, d, v): ")

# If the user chooses the calculate mass, 
if mdv == 'm':

    # Ask the user for the density
    d = float(input("Density: "))

    # Ask the user for the volume
    v = float(input("Volume: "))

    # Result is: (density * volume)
    result = ("Mass is: " + str(d*v))

# Else, if the user chooses to calculate the density,    
elif mdv == 'd':

    # Ask the user for the mass
    m = float(input("Mass: "))

    # Ask the user for the volume
    v = float(input("Volume: "))

    # Result is: (mass / volume)
    result = ("Density is: " + str(m/v))

# Else if the user chooses to calculate the volume, 
elif mdv == 'v':

    # Ask the user for the mass
    m = float(input("Mass: "))

    # Ask the user for the density 
    d = float(input("Density: "))

    # Result is: 
    result = ("Volume is: " + str(m/d))

# Print the result 
print(result)
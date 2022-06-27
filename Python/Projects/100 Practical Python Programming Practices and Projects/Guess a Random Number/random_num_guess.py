# Import the random integer library 
from random import randint

# Create variable to store a random integer between 1 and 100
guess_num = randint(1, 100)

# Variable to take integer guess from user
user_input = 0

# Track the amount of attempts taken to guess the correct integer 
trial_period = 1

# While the correct integer we're looking for is not the user's guess
while guess_num != user_input:

    # Print the attempt number 
    print("The trial no %d: " %trial_period, end="")

    # Ask the user to guess the correct integer 
    user_input = int(input())

    # If the user's guess is less than the correct integer
    if user_input < guess_num:

        # Print that it is less than the correct integer 
        print("The input number is too low")

    # Else, if the user's guess is greater than the correct integer
    elif user_input > guess_num:

        # Print that it is greater than the correct integer 
        print("The input number is too high")

    # Else, print that it is the correct guess
    else:
        print("Good job! That's the correct guess!")
    
    # Increment the attempt number 
    trial_period += 1



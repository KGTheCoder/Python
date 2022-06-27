# Binary search implementation

def binarySearch(array, x):

    # Establish the low and high index of array 
    low = 0
    high = len(array) - 1

    # While the low value is less than or equal to the high value,
    while low <= high:

        # Initialize the middle value by splitting the array in half
        mid = low + (high - low) // 2

        # If the middle value is the value we're looking for, return it
        if array[mid] == x:
            return mid

        # Otherwise, if the middle value is less than the value we're looking for,    
        elif array[mid] < x:

            # Set low to the middle value plus 1
            low = mid + 1
        else:
            high = mid - 1
    return -1


array = [3, 16, 25, 61, 90, 101, 299, 394, 900]
print(binarySearch(array, 90))
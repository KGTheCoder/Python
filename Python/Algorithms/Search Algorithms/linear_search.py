# linear search implementation

def search(arr, x):

    # Iterate through each valuue in the array
    for i in range(len(arr)):

        # If the value we're looking for is found, return its index
        if arr[i] == x:
            return i

    # Otherwise, return nil if value is not found
    return -1

array = [3, 17, 75, 80, 202, 500, 300]
print(search(array, 75))


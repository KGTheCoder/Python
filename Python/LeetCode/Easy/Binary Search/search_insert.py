def search_insert(arr, x):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 6]
print(search_insert(arr, 5))


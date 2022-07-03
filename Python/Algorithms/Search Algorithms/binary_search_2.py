def binarySearch(arr, l, r, x):
    while l <= r:
        mid = 1 + (r - 1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return -1


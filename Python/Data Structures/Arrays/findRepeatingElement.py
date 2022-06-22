def findRepeatingElement(arr, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2


    if (arr[mid] != mid + 1):

        if (mid > 0 and arr[mid]==arr[mid-1]):
            return mid

        return findRepeatingElement(arr, low, mid-1)

    return findRepeatingElement(arr, mid+1, high)

arr = [1, 2, 3, 3, 4, 5]
n = len(arr)
index = findRepeatingElement(arr, 0, n-1)
if (index is not -1):
    print (arr[index])

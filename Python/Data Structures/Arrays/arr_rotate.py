"""
def rotate(L, d, n):
    k = L.index(d)
    new_lis = []
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    size = len(arr)

    arr = rotate(arr, d, size)
    print(arr)
"""

def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = x

arr = [1, 2, 3, 4, 5]
n = len(arr)
print("Given array: " + str(arr))

rotate(arr, n)

print("\nRotated array: " + str(arr))
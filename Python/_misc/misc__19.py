"""
fruits = ['apples', 'banana', 'cherry']

x = fruits.index('cherry')
print(x)
"""
"""
L = [1, 2, 3, 4, 5, 6, 7]
d = 2
k = L.index(d)

print("k = " + str(k))

new_lis = []
new_lis = L[k+1:] + L[0:k+1]

print("new_lis = " + str(new_lis))
"""

arr = [1, 2, 3, 4, 5]

def rotate(arr, n):
    x = arr[n - 1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = x

n = len(arr)

from random import random 

n = 20
arr = []
for x in range(n):
    arr.append(int(random()*100))

arr.sort()
print(arr)

num = int(input("Search for any number in the array: "))

min = 0
max = n - 1

while min <= max:
    mid = (min + max) // 2
    if num < arr[mid]:
        max = mid - 1
    elif num > arr[mid]:
        min = mid + 1
    else:
        print("The number is located at index: ", mid)
        break
else:
    print("Sorry, that number does not exist")
arr_1 = [1, 5, 6, 9, 11]
arr_2 = [3, 4, 7, 8, 10]

print("Here is the orginal arr_1: " + str(arr_1))
print("Here is the original arr_2: " + str(arr_2))

size_1 = len(arr_1)
size_2 = len(arr_2)

res = []
i, j = 0, 0

while i < size_1 and j < size_2:
    if arr_1[i] < arr_2[j]:
        res.append(arr_1[i])
        i += 1
    else:
        res.append(arr_2[j])
        j += 1

res = res + arr_1[i:] + arr_2[j:]

print("Here is the sorted and merged list: " + str(res))
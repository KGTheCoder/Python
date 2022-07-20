"""
def addition(n):
    return n + n

nums = (1, 2, 3, 4)
result = map(addition, nums)
print(list(result))
"""

"""
nums = [1, 2, 3, 4, 5]
squared = []

for num in nums:
    squared.append(num **2)

print(squared)

# --------------------

def square(num):
    return num **2

nums = [1, 2, 3, 4, 5]
squared = map(square, nums)

print(list(squared))
"""

"""
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = map(int, str_nums)

print(list(int_nums))
"""

"""
nums = [-2, -1, 0, 1, 2]

abs_values = list(map(abs, nums))
print(abs_values)

print(list(map(float, nums)))

words = ["Welcome", "to", "My", "World"]
print(list(map(len, words)))
"""

"""
nums = [1, 2, 3, 4, 5]
squared = map(lambda num: num **  2, nums)

print(list(squared))
"""

"""
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

print(list(map(pow, first_it, second_it)))
"""

"""
print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))
print(list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7,8])))
"""



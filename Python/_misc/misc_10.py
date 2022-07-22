values = ["a", "b", "c"]

"""
for value in values:
    print(value)

# -------------
index = 0

for value in values:
    print(index, value)
    index += 1

# -------------
index = 0

for value in values:
    print(index, value)

# -------------
"""

"""
index = 0

for index in range(len(values)):
    value = values[index]
    print(index, value)

print("---------------------------------")
for count, value in enumerate(values):
    print(count, value)

print("---------------------------------")
for count, value in enumerate(values, start=1):
    print(count, value)

print("---------------------------------")
users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user)
"""

nums = [2, 7, 11, 15]
for i, n in enumerate(nums):
    print(i, n)
'''
things = ['apples', 'baboons', 'cribs', 'dulcimers']

for thing in things:
    print("Here's a thing: %s" % thing)
'''

'''
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True 
'''

# Constant time O(1)
def OddorEven(n):
    return "Even" if n % 2 else "Odd"


# Logarithmic time O(logn)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint + 1
    return found

# Linear time O(n)
a = [2, 16, 7, 9, 8, 23, 12]
max_item = a[0]
for item in a:
    if item > max_item:
        max_item = item 
print(max_item)

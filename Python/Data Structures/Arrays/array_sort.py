# sorts the list (default = ascending)

nums = ["3", "35", "99", "100", "1"]

print(nums)
nums.sort()

print(nums)

# A function that returns the 'year' value:
def myFunc(e):
    return e['year']

cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

print(cars)
cars.sort(key=myFunc)

print(cars)
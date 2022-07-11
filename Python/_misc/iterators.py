mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit_2 = iter(mystr)

print(next(myit_2))
print(next(myit_2))
print(next(myit_2))
print(next(myit_2))
print(next(myit_2))
print(next(myit_2))

for x in mytuple:
    print(x)



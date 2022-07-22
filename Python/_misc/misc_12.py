'''
key = 'the quick brown fox jumps over the lazy dog'
print(len(key))
'''

'''
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("model")
print(x)

y = car.get("price", 15000)
print(y)
'''

'''
dic = {"A": 1, "B": 2}
print(dic.get("A"))
print(dic.get("B"))
'''

test_dict = {"Coffee" : {"is" : "the best!"}}
print("This is the original dictionary: " + str(test_dict))

res = test_dict.get("Coffee", {}).get("is")
print("This is the nested value: " + str(res))
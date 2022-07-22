key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

'''
map = {}
temp = "a"

for i in range(len(key)):
    if key[i] != " " and map.get(key[i]) == None:
        map[key[i]] = temp
        temp = chr(ord(temp) + 1)

print(temp)
print("-----------------")

temp_2 = "a"
temp_2 = (ord(temp_2) + 1)
print(temp_2)
temp_2 = chr(temp_2)
print(temp_2)
'''

'''
hashT = {" ": " "}
i = 97
for k in key:
    if k not in hashT and k != ' ':
        hashT[k] = chr(i)
        i += 1

print(hashT)
'''

dic = {}
seq = 97
res = ""

for c in key:
    if c not in dic and c != " ":
        dic[c] = dic.get(c, 0)

print(dic)
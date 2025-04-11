arr =[22,33,22,5,33]
dic = {}
for i in arr:
    dic[i] = dic.get(i,0)+1
print(dic)

for keys, values in dic.items():
    if values == 1:
        print(keys)


#####XOR numbers , the one which only occurs once, return that

xor = 0
for i in arr:
    xor=i^xor
print(xor)
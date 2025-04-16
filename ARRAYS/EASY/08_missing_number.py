arr = [4,2,5,1]

### Brute Force
max1 = max(arr)
# print(max1)
# dic = {}
# for i in arr:
#     dic[i]=dic.get(i,0)+1
# print(dic)
# for i in range(1,max1):
#     if dic.get(i,0)==0:
#         print(i)

###Sum Method
sum1 =sum2= 0
for i in arr:
    sum1 +=i
for i in range(max1+1):
    # print(i)
    sum2 +=i
# print(sum2, sum1)
print(sum2-sum1)

###XOR method
xor1=xor2=0
for i in range(1,max1+1):
    xor2 = xor2^i
for i in arr:
    xor1 = xor1^i
print(xor2^xor1)



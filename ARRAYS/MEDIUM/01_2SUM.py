# arr = [2,6,5,8,11]
arr =[2,5,6,8,11]
temp = {}
target = 14

##Brute Force
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)

# Hashing
for i in range(len(arr)):
    subs = target-arr[i]
    if subs in temp:
        print( i, temp.get(subs))
    temp[arr[i]] = i

# 2 pointer approach
left = 0
right = len(arr)-1
while left<right:
    if arr[left]+arr[right]< target:
        left+=1
    elif arr[left]+arr[right]> target:
        right-=1
    else:
        print("YES")
        break

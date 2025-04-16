arr=[2,2,3,3,1,2,2]
#Brute
for i in range(len(arr)):
    count1 = 0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count1+=1
    if count1> (len(arr))/2:
        print( arr[i])
        break

#Hashing
temp={}
for i in range(len(arr)):
    temp[arr[i]]=temp.get(arr[i],0)+1

for key, value in temp.items():
    if value>len(arr)/2:
        print(key, value)
        break
# print(temp)


#Moore's Algo
def majorityElement(self, nums):
    ele = count = 0
    for i in range(len(nums)):
        if count==0:
            count=1
            ele = nums[i]
            
        elif nums[i]==ele:
            count+=1
        else:
            count-=1
    act_count = 0
    for num in nums:
        if ele == num:
            act_count+=1
    if act_count>len(nums)//2:
        return ele
    else:
        return None
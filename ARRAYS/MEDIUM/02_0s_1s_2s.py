arr =[0,1,2,0,1,2,1,0,0,0,1]
#Brute
# count0 = 0
# count1=0
# count2 = 0
# count0= sum([1 for x in arr if x==0])
# count1= sum([1 for x in arr if x==1])
# count2= sum([1 for x in arr if x==2])

# for i in range(count0):
#     arr[i] = 0
# for j in range(count0,count0+count1):
#     arr[j]=1
# for k in range(count0+count1, count0+count1+count2):
#     arr[k]=2

# print(arr) 

#Dutch National Flag Algo

low=0
mid=0
high = len(arr)-1

while mid<=high:
    if arr[mid]==0:
        arr[low], arr[mid]=arr[mid], arr[low]
        low+=1
        mid+=1
    elif arr[mid]==1:
        mid+=1
    else:#if arr[mid]==2:
        arr[mid], arr[high]=arr[high], arr[mid]
        high-=1
print(arr)
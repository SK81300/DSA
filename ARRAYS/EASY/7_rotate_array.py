arr = [1,4,5,2,4,64,6]

# """Rotate array by one position"""
# temp = arr[0]
# for i in range(1,len(arr)):
#     arr[i-1]=arr[i]
# arr[-1]=temp
# print(arr)


"""Rotate D Places"""
d = 3
# Get the first d elements in temp array
n =len(arr)
temp = []
for i in range(d):
    temp.append(arr[i])

# After the d places, the D+1 element will go to 0th index, so it will be i-d index

for i in range(d, len(arr)):
    arr[i-d]=arr[i]

# Now we need to go though the temp array and places the elements at the end of original array
j=0
for i in range(n-d, len(arr)):
    arr[i]=temp[j]
    j+=1
print(arr)

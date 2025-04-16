arr = [3,1,-2,-5,2,-4]

#Brute
# pos = [x for x in arr if x>0]
# neg = [x for x in arr if x<0]

# for i in range(len(arr)//2):
#     arr[2*i]= pos[i]
#     arr[2*i+1]= neg[i]

print(arr)

#Optimal
# n = len(arr)
# ans = [0]*n
# pos =0
# neg = 1
# for i in range(len(arr)):
#     if arr[i]>0:
#         ans[pos]=arr[i]
#         pos+=2
#     else:
#         ans[neg]=arr[i]
#         neg+=2
# print(ans)

# Rearrange elements when the number of positives and negatives are not equal

pos = [x for x in arr if x>0]
neg = [x for x in arr if x<0]

if len(pos)> len(neg):
    for i in range(len(neg)):
        arr[2*i]= pos[i]
        arr[2*i+1]= neg[i]
    
    

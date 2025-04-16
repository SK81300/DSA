import sys
nums = [-2,-3,4,-1,-2,1,5,-3]
#Brute
# def maxSubArray( nums):
#     max1 = -sys.maxsize-1
#     for i in range(len(nums)):
#         for j in range(i, len(nums)+1):
#             sum1 = 0
#             for k in range(i,j):
#                 sum1+=nums[k]
#             max1 = max(sum1, max1)
#     return max1

# print(maxSubArray(nums))

#Kadane

# current_sum = maxi=nums[0]
# for i in range(len(nums)):
#     current_sum= max(nums[i], current_sum+nums[i])
#     maxi = max(maxi, current_sum)

# print(maxi)

#Print subarray as well as sum
def max_subarray(nums):

    maxi= curr_sum = nums[0]
    start = end =s =0
    for i in range(len(nums)):
        if nums[i]> curr_sum+nums[i]:
            curr_sum= nums[i]
            s=i
        else:
            curr_sum+=nums[i]

        if curr_sum>maxi:
            maxi=curr_sum
            start =s
            end =i
    return maxi, nums[start:end+1]

print(max_subarray(nums))

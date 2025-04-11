arr = [1,2,3,1,1,1,5]
k=3
def longest_subarray(arr):
    left = right = max_len=current_sum = 0
    while right < len(arr):
        current_sum +=arr[right]
        # Shrink the window size of current_sum increases than k
        while left <= right and current_sum > k:
            current_sum-=arr[left]
            left +=1

        # If current_sum=k
        if current_sum==k:
            max_len = max(max_len,right-left+1)
        right +=1
    return max_len

print(longest_subarray(arr))
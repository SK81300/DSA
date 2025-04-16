'''We are using 2 pointer approach where the first counter will go through the array
We are considering first element to be unique
From 2nd element, we will check each element from previous and if it is not equal we will push it to the (i+1) index and then increment j
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for j in range(1, len(nums)):
            if nums[j]!=nums[i]:
                nums[i+1]=nums[j]
                i+=1
        return i+1
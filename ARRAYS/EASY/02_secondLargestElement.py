#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # # Code Here
        # largest = 0
        # sec = -1
        
        # for i in range(len(arr)):
        #     if arr[i]> largest:
        #         largest=arr[i]
                
        # for i in range(len(arr)):
        #     if arr[i]>sec and arr[i]!= largest:
        #         sec = arr[i]
        # return sec
        largest  = arr[0]
        second = -1
        for i in range(len(arr)):
            if arr[i]> largest and arr[i]> second:
                second = largest
                largest = arr[i]
            elif arr[i]<largest and arr[i]> second:
                second = arr[i]
        return second

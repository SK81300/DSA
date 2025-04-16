class solution:
    def sortedArray(arr):
        for i in range(len(arr)):
            if arr[i-1]>arr[i]:
                return False
        return True

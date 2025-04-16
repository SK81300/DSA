arr = [7,1,5,3,6,4]
def stocks(arr):
    mini = arr[0]
    maxProfit = 0
    for i in range(1,len(arr)):
        cost=arr[i]-mini
        maxProfit = max(maxProfit,cost)
        mini=min(mini, arr[i])

    return maxProfit

print(stocks(arr))
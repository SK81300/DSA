def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    max_len = 0
    sum_index_map = {}  # stores first occurrence of a prefix sum

    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If the subarray from the beginning has sum k
        if prefix_sum == k:
            max_len = i + 1

        # If prefix_sum - k seen before, subarray between those indices has sum k
        if (prefix_sum - k) in sum_index_map:
            max_len = max(max_len, i - sum_index_map[prefix_sum - k])

        # Store the first occurrence of prefix_sum
        if prefix_sum not in sum_index_map:
            sum_index_map[prefix_sum] = i

    return max_len


"""
Prefix Sum: This is the sum of all elements from index 0 to the current index i. We'll keep updating this as we move through the array.

If at any index i, we have:

prefix_sum[i] - prefix_sum[j] = k, then the subarray from index j + 1 to i has sum k.

We use a hashmap (sum_index_map) to store the first index where each prefix sum appears. Why first? Because we want the longest subarray, so we want the earliest start possible.
"""

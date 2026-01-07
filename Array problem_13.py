'''
Problem

Given an array of integers and an integer K, find the length of the longest subarray whose sum is exactly K.

Example:
Input: arr = [1, -1, 5, -2, 3], K = 3
Output: 4
(Subarray: [1, -1, 5, -2])
'''
def longest_subarray_sum_k(arr, k):
    prefix_sum = 0
    index_map = {}
    max_len = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if prefix_sum == k:
            max_len = i + 1

        if prefix_sum - k in index_map:
            max_len = max(max_len, i - index_map[prefix_sum - k])

        if prefix_sum not in index_map:
            index_map[prefix_sum] = i

    return max_len


# Example usage
arr = [1, -1, 5, -2, 3]
k = 3
print("Longest Subarray Length =", longest_subarray_sum_k(arr, k))

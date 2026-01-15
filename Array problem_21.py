def longest_unique_subarray(arr):
    window = set()
    left = 0
    max_len = 0

    for right in range(len(arr)):
        while arr[right] in window:
            window.remove(arr[left])
            left += 1

        window.add(arr[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Example
arr = [4, 2, 1, 2, 5, 3, 5, 1, 2]
print(longest_unique_subarray(arr))

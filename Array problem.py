'''
Problem:
Given an array of integers, reverse the array.

Example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
'''
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))


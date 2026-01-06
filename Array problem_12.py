'''
Problem

An index is called an equilibrium index if the sum of elements on its left is equal to the sum of elements on its right.

Example:
Input: [1, 3, 5, 2, 2]
Output: 2
'''
def equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        total_sum -= arr[i]
        if left_sum == total_sum:
            return i
        left_sum += arr[i]

    return -1


# Example usage
arr = [1, 3, 5, 2, 2]
print("Equilibrium Index =", equilibrium_index(arr))


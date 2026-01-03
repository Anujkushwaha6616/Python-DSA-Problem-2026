def second_largest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return None

    return second


# Example usage
arr = [10, 5, 20, 8, 20]
print("Second Largest =", second_largest(arr))

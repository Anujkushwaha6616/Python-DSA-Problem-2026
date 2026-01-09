def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in num_set:  # start of a sequence
            current = n
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest

arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(arr))

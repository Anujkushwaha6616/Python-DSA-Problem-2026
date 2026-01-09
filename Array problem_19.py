def subarrays_with_sum(arr, target):
    result = []
    prefix_sum = 0
    mp = {0: [-1]}

    for i, val in enumerate(arr):
        prefix_sum += val

        if prefix_sum - target in mp:
            for start in mp[prefix_sum - target]:
                result.append(arr[start+1:i+1])

        if prefix_sum not in mp:
            mp[prefix_sum] = []
        mp[prefix_sum].append(i)

    return result

arr = [1, 2, 3, -3, 4, -2, 2]
target = 3
ans = subarrays_with_sum(arr, target)
for sub in ans:
    print(sub)

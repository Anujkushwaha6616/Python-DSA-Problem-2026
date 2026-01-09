'''
Problem Statement:

You are given an array with both positive and negative numbers.
Rearrange the array so that numbers appear in this order:
positive, negative, positive, negative...
Order does not need to be maintained.

Example

Input:
arr = [3, 1, -2, -5, 8, -9]

Output:
[3, -2, 1, -5, 8, -9]
'''
def rearrange_alt(arr):
    pos = []
    neg = []

    for x in arr:
        if x >= 0:
            pos.append(x)
        else:
            neg.append(x)

    res = []
    i = j = 0
    turn_pos = True  # start with positive

    while i < len(pos) or j < len(neg):
        if turn_pos and i < len(pos):
            res.append(pos[i])
            i += 1
        elif not turn_pos and j < len(neg):
            res.append(neg[j])
            j += 1
        elif i < len(pos):
            res.append(pos[i])
            i += 1
        else:
            res.append(neg[j])
            j += 1

        turn_pos = not turn_pos

    return res

arr = [3, 1, -2, -5, 8, -9]
print(rearrange_alt(arr))


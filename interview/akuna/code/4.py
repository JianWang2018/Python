def closest_subtring(arr, target):
    i = j = 0
    partial_sum = arr[0]
    min_diff = abs(target - partial_sum)
    index = (i, j)
    while i<j+2:
        if partial_sum < target:
            if j != len(arr) - 1:
                j += 1
                partial_sum += arr[j]
            else:
                break
        elif partial_sum > target:
            if i != len(arr) - 1:
                partial_sum -= arr[i]
                i += 1
            else:
                break
        else:
            return i, j
        if abs(partial_sum - target) < min_diff:
            min_diff = abs(partial_sum - target)
            index = (i, j)
    return index
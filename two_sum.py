def two_sum(nums, target):
    table = {}
    for i in range(len(nums)):
        if nums[i] not in table:
            table[target - nums[i]] = i
        else:
            return [i, table[nums[i]]]


arr = [2, 7, 11, 15]
print(two_sum(arr, 9))
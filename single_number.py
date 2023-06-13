def single_number(nums):
    c = 0
    for i in range(len(nums)):
        c = c ^ nums[i]
    return c


arr = [4, 2, 1, 2, 1]
print(single_number(arr))

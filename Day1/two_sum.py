def two_sum(nums, target):
  length = len(nums)
  for i in range(0, length-1):
    j = i + 1
    for j in range(1, length):
      if target == nums[i] + nums[j]:
        return [i, j]


print(two_sum([4, 9, 11, 14], 13))
    
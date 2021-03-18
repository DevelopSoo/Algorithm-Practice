def move_zeroes(nums):
  i = 0
  j = 0
  while i < len(nums):
    if nums[i] != 0:
      temp = nums[i] # 임시로 삽입할 값 저장
      del nums[i]    # 0이 아닌 값 삭제
      nums.insert(j, temp)
      i += 1
      j += 1
    else:
      i += 1
  
  return nums




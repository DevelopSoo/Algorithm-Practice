def more_than_half(nums):
  # 아래 코드를 입력해주세요.
  check_num_count = {}

  for i in nums:
    if i in check_num_count:
      check_num_count[i] += 1
    else:
      check_num_count[i] = 1
  
  for key, val in check_num_count.items():
    if val/len(nums) > 1/2:
      return key

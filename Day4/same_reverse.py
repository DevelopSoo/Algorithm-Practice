def same_reverse(num):
  # 우선 num을 문자열로 변환
  num_str = str(num)

  if num_str == num_str[::-1]:
    return True
  return False


  
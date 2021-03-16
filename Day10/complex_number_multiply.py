def complex_number_multiply(a, b):
  """a의 숫자 부분 구하기"""
  a_split_list = a.split("+")
  a_first_num  = int(a_split_list[0])
  a_second_num = int(a_split_list[1][:-1])

  b_split_list = b.split("+")
  b_first_num  = int(b_split_list[0])
  b_second_num = int(b_split_list[1][:-1])

  result_first_num = (a_first_num * b_first_num) + (-a_second_num * b_second_num)

  result_second_num = (a_first_num * b_second_num) + (a_second_num * b_first_num)

  return f"{result_first_num}+{result_second_num}i"


"""처음에 풀었던 방법. 하지만 이 방법으로 풀면 두 자리 수 이상은 구할 수 없다."""
  # if a[0] == '-':
  #   a_first_num = int(a[0]+a[1])
  #   if a[3] == '-':
  #     a_second_num = int(a[3]+a[4])
  #   else:
  #     a_second_num = int(a[3])
  # else:
  #   a_first_num = int(a[0])
  #   if a[2] == '-':
  #     a_second_num = int(a[2]+a[3])
  #   else:
  #     a_second_num = int(a[2])
  
  # """b의 숫자 부분 구하기"""
  # if b[0] == '-':
  #   b_first_num = int(b[0]+b[1])
  #   if b[3] == '-':
  #     b_second_num = int(b[3]+b[4])
  #   else:
  #     b_second_num = int(b[3])
  # else:
  #   b_first_num = int(b[0])
  #   if b[2] == '-':
  #     b_second_num = int(b[2]+b[3])
  #   else:
  #     print(b[2])
  #     b_second_num = int(b[2])

  
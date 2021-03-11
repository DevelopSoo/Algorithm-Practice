import operator


def top_k(nums, k):
  num_count = {}

  """숫자와 그 개수를 딕셔너리로 만들어줌"""
  for i in nums:
    if i in num_count:
      num_count[i] += 1
    else:
      num_count[i] = 1

  """개수를 기준으로 내림차순 정렬함"""
  sorted_num_count = sorted(num_count.items(), key=operator.itemgetter(1), reverse=True)

  """리스트 내에 튜플의 형태임. 그래서 각 튜플의 첫 번째 인자(숫자)를 새로운 리스트에 넣고 반환 """
  num_list = []
  for i in range(k):
    num_list.append(sorted_num_count[i][0])


  return num_list
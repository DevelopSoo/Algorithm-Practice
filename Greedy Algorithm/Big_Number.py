"""
알고리즘 책 p.92
배열의 크기 N, 더해지는 횟수 M, 특정 인덱스에 해당하는 숫자가 연속으로 최대 더해지는 횟수 K
"""

N, M, K = map(int, input().split())

n_list= list(map(int, input().split()))

n_list.sort(reverse=True)

first = n_list[0]
second = n_list[1]

max_num = 0
count = 0
for i in range(M):
    count += 1
    if count < K:
        max_num += first
    else:
        max_num += second
        count = 0

print(max_num)

# 틀림 -> 두 번째로 큰수를 잘못 더함

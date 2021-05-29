# N 행의 개수(가로 수), M 열의 개수(세로 수)

N, M = map(int, input().split())

# 이중 리스트
NM_list = []
# N행의 리스트
N_list = []
for _ in range(N):
    N_list = list(map(int, input().split()))
    NM_list.append(N_list)

# min() 메소드로 좀 더 짧게 할 수 있음
min_list = []
for i in NM_list:
    min_list.append(min(i))

print(max(min_list))

        
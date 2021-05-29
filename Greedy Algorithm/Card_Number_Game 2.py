# N 행의 개수(가로 수), M 열의 개수(세로 수)

N, M = map(int, input().split())

# 이중 리스트
NM_list = []
# N행의 리스트
N_list = []
for _ in range(N):
    N_list = list(map(int, input().split()))
    NM_list.append(N_list)


min_list = []
for i in range(len(NM_list)):
    min_num = 100 # 가장 작은 수를 비교하기 위해 미리 설정
    for j in NM_list[i]:
        if min_num > j:
            min_num = j
    min_list.append(min_num)

print(max(min_list))

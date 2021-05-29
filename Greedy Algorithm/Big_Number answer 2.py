"""
알고리즘 책 p.92
배열의 크기 N, 더해지는 횟수 M, 특정 인덱스에 해당하는 숫자가 연속으로 최대 더해지는 횟수 K
"""

N, M, K = map(int, input().split())

n_list= list(map(int, input().split()))

n_list.sort() # 입력받은 수들 정렬하기
first = n_list[N-1]
second = n_list[N-2]

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1 # 더할 때마다 1씩 빼기
    if M == 0:
        break
    result += second
    M -= 1

print(result)


"""
알고리즘 책 p.92
배열의 크기 N, 더해지는 횟수 M, 특정 인덱스에 해당하는 숫자가 연속으로 최대 더해지는 횟수 K
"""

n, m, k = list(map(int, input().split()))

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k # 만약 k가 3이면 6, 6, 6, 5까지 하나의 수열이므로 k+1로 4이다. m이 10이면 수열이 2번 도는 것. 그리고 가장 큰 수가 더해질 수 있는 횟수 k를 곱한다.
count += m%(k+1) # 만약 m이 10이고 k+1이 4라면 2가 남고, 그만큼 가장 큰 수를 더한다.

result = 0 
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 그 다음 큰 수 더하기

print(result)


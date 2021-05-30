"""
move.py보다 나은 점
1. move_types를 미리 설정해놓음으로써 L, R, U, D의 의미파악이 좀 더 쉬움
2. 이후에 몇 칸을 움직일 지 변할 때 수정이 쉽다.
"""

# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split() # 이동할 방향들

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 예시
    if nx < 1 or ny < 1 or nx > n or ny > y:
        continue
    x, y = nx, ny

print(x, y)


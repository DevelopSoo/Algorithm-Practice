"""
나동빈 p.115
왕실의 나이트 문제
"""

"""
최대 경우의 수 8가지

1. 세로 1 -> -4 
2. 세로 2 -> -2 (위로 못움직임)
3. 세로 7 -> -2 (아래로 못움직임)
4. 세로 8 -> -4 

5. 가로 a -> -4
6. 가로 b -> -2(좌로 못움직임)
7. 가로 g -> -2
8. 가로 h -> -4(우로 못움직임)

"""
minus_four_num = ['1','8']
minus_two_num = ['2', '7']

minus_four_str = ['a', 'h']
minus_two_str = ['b', 'g']

# 원래 크기
count = 8

location = input()

for s in location:
    if s in minus_four_num:
        count -= 4
    elif s in minus_two_num:
        count -= 2

    if s in minus_four_str:
        count -= 4
    elif s in minus_two_str:
        count -= 2

if count == 0:
    count = 2

print(count)


# 나동빈 p.111

n = int(input())
directions = list(input().split())

x = 1
y = 1

for d in directions:
    if d == "R" and y >= 5:
        continue
    elif d == "R":
        y += 1

    if d == "L" and y <= 1:
        continue
    elif d == "L":
        y -= 1

    if d == "U" and x <= 1:
        continue
    elif d == "U":
        x -= 1

    if d == "D" and x >= 5:
        continue
    elif d == "D":
        x += 1

print(x, y)
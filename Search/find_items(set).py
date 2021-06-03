# 나동빈 책 p.197

n = int(input())
array = set(map(int, input().split()))

m = int(input())
items_to_find = list(map(int, input().split()))

for i in items_to_find:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
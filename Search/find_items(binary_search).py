# 나동빈 책 p.197

# 이진탐색으로 찾기
import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)



n = int(input())
items = list(map(int, sys.stdin.readline().split()))

m = int(input())
items_to_find = list(map(int, sys.stdin.readline().split()))

# 정렬
items.sort()

for i in items_to_find:
    result = binary_search(items, i, 0, n-1)
    if result != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")
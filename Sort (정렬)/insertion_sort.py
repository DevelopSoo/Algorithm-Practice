# 삽입 정렬: 삽입 정렬은 특정한 데이터를 적절한 위치에 '삽입'하는 것을 말한다.
# 이때 왼쪽(앞) 데이터는 이미 정렬된 것이라고 가정한다.

array = [7, 5, 9, 6, 3, 2, 4, 1, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)


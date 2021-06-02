# 선택정렬 : 선택정렬은 '가장 작은 수'를 선택하여 맨 앞으로 보내는 것이다.

array= [7, 5, 9, 6, 3, 2, 4, 1, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        
    array[i], array[min_index] = array[min_index], array[i]

print(array)

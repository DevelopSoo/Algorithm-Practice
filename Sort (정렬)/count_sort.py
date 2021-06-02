# 계수 정렬: 데이터를 직접 비교하는 것이 아니라 0 ~ 가장 큰 데이터를 리스트의 인덱스로 저장하여 개수를 확인한다.

array =[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count_list = [0] * (max(array)+1)

for i in array:
    count_list[i] += 1

for i in range(len(count_list)):
    for j in range(count_list[i]):
        print(i, end=' ')
    
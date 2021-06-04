t = int(input())

# 각 숫자의 개수들
zero_count = [1,0]
one_count = [0,1]

for i in range(t):
    n = int(input())
    # 이전에 구해놓은 zero_count들이 있는지 확인하기 위함
    length = len(zero_count)
    if length <= n:
        for j in range(length, n+1):
            zero_count.append(zero_count[j-1]+zero_count[j-2])
            one_count.append(one_count[j-1]+one_count[j-2])
        
    
    print(zero_count[n], one_count[n])
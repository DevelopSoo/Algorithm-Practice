# 백준 1003번

t = int(input())

# 인덱스 0 ~ 40까지의 값 초기 세팅(모두 0)
d = [0]*41
# 1을 넣으면 1이 출력되므로 1로 설정, fib(0)은 0이므로 그대로 놔둔다.
d[1] = 1

# 0의 개수와 1의 개수
count_0 = 0
count_1 = 0

def fib(x):    
    if x == 0:
        global count_0
        count_0 += 1
        return 0
    elif x == 1:
        global count_1
        count_1 += 1
        return 1
    else:
        if d[x] != 0:
            return d[x]
        return fib(x-1) + fib(x-2)
    
for i in range(t):
    n = int(input())
    fib(n)
    print(count_0, count_1)
    count_0 = 0
    count_1 = 0
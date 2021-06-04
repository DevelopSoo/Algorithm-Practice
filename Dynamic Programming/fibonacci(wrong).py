t = int(input())

# 
zero_count = [1,0]
one_count = [0,1]

for i in range(t):
    n = int(input())
    for j in range(2, n+1):
        
        zero_count.append(zero_count[j-1]+zero_count[j-2])
        one_count.append(one_count[j-1]+one_count[j-2])
       
    print(zero_count[n], one_count[n])
    


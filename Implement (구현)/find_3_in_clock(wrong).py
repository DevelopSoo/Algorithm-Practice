n = int(input())

"""
n은 0~23까지 가능

01:00:03 => 7    => 7 * 53 = 371개
01:03:01 => 60   => 60 * 7 => 420개
03:00:00 ->60*60 => 3600개

"""

three_contains = [3, 13, 23, 30, 33, 43, 53]

count = 0

for i in range(n+1):
    if i in three_contains:
        count += 3600
    else:
        count += 771

print(count)
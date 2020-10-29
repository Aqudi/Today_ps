N, K = map(int, input().split())
H = 0

C = 0
while True:
    cnt = 0
    temp = N
    while temp > 0:
        if  temp % 2 != 0:
            cnt += 1
        temp //= 2      

    if cnt <= K:
        break
    N += 1
    C += 1
print(C)

N, K = map(int, input().split())
count = 0
while N != 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        t = N % K
        N -= t
        count += t
print(count)
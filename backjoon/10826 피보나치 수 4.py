N = int(input())
fibo = [0, 1, 1] + [-1 for i in range(N-2)]
for n in range(1, N+1):
    if fibo[n] == -1:
        fibo[n] = (fibo[n-1] + fibo[n-2]) % 100000
print(fibo[N])

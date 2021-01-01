N = int(input())
p = [0 for i in range(N+2)]
p[0], p[1] = 0, 1
for i in range(2, N+1):
    p[i] = p[i-2] + p[i-1]
print(p[N])
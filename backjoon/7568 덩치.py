N = int(input())
datas = [tuple(map(int, input().split())) for i in range(N)]
ranks = [1 for _ in range(N)]
for i in range(N):
    a, b = datas[i]
    for j in range(i + 1, N):
        a2, b2 = datas[j]
        if a > a2 and b > b2:
            ranks[j] += 1
        elif a < a2 and b < b2:
            ranks[i] += 1
print(" ".join(map(str, ranks)))

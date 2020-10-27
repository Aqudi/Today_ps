N,M = map(int, input().split())
vsets = [set() for x in range(0, N+1)]
for i in range(M):
    v, u = map(int, sorted(input().split()))
    vsets[v].add(u)

count = 0
for vi in range(1, N+1):
    vneighbor = vsets[vi]
    for ui in list(vneighbor):
        uneighbor = vsets[ui]
        count += len(vneighbor & uneighbor)
print(count)

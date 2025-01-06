n = int(input())

counts = [*range(n, 0, -1), *range(1, n+1)]
lines = map(lambda x: list(x*'*'), counts)

for line in lines:
    print(' '.join(line))
    
def solve(a, b):
    if a[0] < b[0]:
        a[0] += 10
        b[0] *= 2
    else:
        b[0] += 10
        a[0] *= 2

a, b = list(map(lambda x: [int(x)], input().split()))
solve(a, b)
print(a[0], b[0])
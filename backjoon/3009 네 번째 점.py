points = [tuple(map(int, input().split())) for _ in range(3)]
xs = sorted(list(map(lambda x: x[1], points)))
a = xs[0]
if xs.count(a) != 1:
    a = xs[2]
ys = sorted(list(map(lambda x: x[0], points)))
b = ys[0]
if ys.count(b) != 1:
    b = ys[2]
print(b, a)

A, B, C = map(int, [input(), input(), input()])
r = str(A*B*C)
for i in range(10):
    print(r.count(str(i)))

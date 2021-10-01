A, B, V = map(int, input().split())
inter = A-B
if (V-A) % inter == 0:
    print((V-A)//inter + 1)
else:
    print((V-A)//inter + 2)

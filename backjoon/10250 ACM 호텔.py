import math

N = int(input())
for i in range(N):
    H, W, N = map(int, input().split())
    w = math.ceil(N / H)
    h = N % H
    if h == 0:
        h = H
    print(f"{h}{w:02d}")
    
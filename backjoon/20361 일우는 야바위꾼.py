import sys
input = sys.stdin.readline
N, X, K = map(int, input().split())
current = X
for i in range(K):
    f, t = map(int, input().split())
    if f == current:
        current = t
    elif t == current:
        current = f
print(current)

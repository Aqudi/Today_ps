import sys

tdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d, m, y = map(int, sys.stdin.readline().rstrip().split())
while f"{d} {m} {y}" != "0 0 0":
    total = d + sum(tdays[:m-1])
    if m > 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
        total += 1
    print(total)
    d, m, y = map(int, sys.stdin.readline().rstrip().split())

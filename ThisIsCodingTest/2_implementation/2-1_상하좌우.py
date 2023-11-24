N = int(input())
i, j = 0, 0
moves = input().split()
for m in moves:
    if m == "R" and j < N-1:
        j += 1
    elif m == "L" and j > 0:
        j -= 1
    elif m == "U" and i > 0:
        i -= 1
    elif m == "D" and i < N-1:
        i += 1
print(i+1, j+1)
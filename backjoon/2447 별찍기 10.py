def solve(N, i, j, scale):
    if (i//scale) % 3 == 1 and (j//scale) % 3 == 1:
        print(" ", end="")
    elif N == scale:
        print("*", end="")
    else:
        solve(N, i, j, scale * 3)


N = int(input())
for i in range(N):
    for j in range(N):
        solve(N, i, j, 1)
    print()

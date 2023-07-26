T = int(input())
kn = [(int(input()), int(input())) for _ in range(T)]
for k, n in kn:
    board = [[0] * n for _ in range(k+1)]
    board[0] = list(range(1, n + 1))
    for i in range(1, k+1):
        for j in range(n):
            board[i][j] = sum(board[i - 1][:j+1])
    print(board[-1][-1])
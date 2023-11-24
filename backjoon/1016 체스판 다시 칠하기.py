import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = []
answer = M * N
for i in range(N):
    board.append(list(input()))

for i in range(N - 7):
    for j in range(M - 7):
        white = 0
        black = 0

        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != "B":
                        black += 1
                    else:
                        white += 1
                else:
                    if board[k][l] != "W":
                        black += 1
                    else:
                        white += 1
        answer = min(answer, white, black)
print(answer)

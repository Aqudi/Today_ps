N, M = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

count = 0
while True:
    # 현재 위치 청소
    if board[y][x] == 0:
        board[y][x] = 2
        count += 1
        continue

    # 청소하러 이동
    move = any(map(lambda dxy: board[y + dxy[1]][x + dxy[0]] == 0, directions))
    if move:
        for i in range(4):
            # 반시계방향으로 회전
            d = (d + 3) % len(directions)
            dx, dy = directions[d]
            ny, nx = y + dy, x + dx

            # 청소가 필요하다면 이동
            if board[ny][nx] == 0:
                x, y = nx, ny
                break
        continue

    # 청소할 칸이 없는 경우
    dx, dy = directions[(d + 2) % len(directions)]
    ny, nx = y + dy, x + dx
    if board[ny][nx] != 1:
        x, y = nx, ny
    else:
        break
print(count)

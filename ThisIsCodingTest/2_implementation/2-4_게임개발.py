N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]
visited = set([(x, y)])


def simulate_go(d, back=False):
    modifier = -1 if back else 1
    dx = x + (modifier * move[d][0])
    dy = y + (modifier * move[d][1])
    newPose = (dx, dy)
    return newPose


canMove = True
while canMove:
    # 사방이 바다이거나 이미 방문한 곳인지 확인
    canMove = False
    for i in range(len(move)):
        lx, ly = simulate_go(i)
        if board[ly][lx] == 0 and (lx, ly) not in visited:
            canMove = True
            break

    # 사방이 바다이거나 이미 방문한 곳이면 방향 유지한 채로 뒤로 이동
    if not canMove:
        lx, ly = simulate_go(d, back=True)
        # 뒤가 바다인 경우에는 움직임을 멈춤
        if board[ly][lx] == 1:
            canMove = False
        x, y = lx, ly
        continue

    # 왼쪽으로 방향을 튼 후 이동
    d = (d + 1) % 4
    newPose = simulate_go(d)
    lx, ly = newPose
    if board[newPose[1]][newPose[0]] == 0 and newPose not in visited:
        visited.add(newPose)
        x, y = newPose

print(len(visited))
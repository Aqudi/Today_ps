import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    answer = 0
    XY = []

    for _ in range(K):
        point = tuple(map(int, input().split()))
        XY.append(point)
        board[point[1]][point[0]] = 1

    for xy in XY:
        if board[xy[1]][xy[0]] != 1:
            continue

        # BFS
        queue = deque([xy])
        while queue:
            x, y = queue.popleft()

            # 지렁이가 지키고 있지 않은 배추일 경우에 1로 설정
            if board[y][x] == 1:
                answer += 1

            # 이미 지렁이가 지키고 있음을 2로 표시
            board[y][x] = 2
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if M > nx >= 0 and N > ny >= 0 and board[ny][nx] == 1:
                    board[ny][nx] = 2
                    queue.append((nx, ny))
    print(answer)

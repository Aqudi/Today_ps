# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 전형적인 BFS, DFS 문제 BFS에서 시간초과가 난다면 이미 방문한 노드를 재방문하고 있을 가능성이 높음
# 이를 방지하기 위해서 노드를 queue에 넣을 때 바로 방문을 선언해줘야 한다.
# 그래야 해당 노드에서부터 시작해서 다음으로 이동하기 전에 queue에 밀려 있는 다른 점들에서 주변을 탐색할 때
# 이 노드를 제외할 수 있다.

from queue import deque


def solution(maps):
    visited = set()

    Y, X = len(maps), len(maps[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, (0, 0))])
    visited.add((0, 0))

    while queue:
        turn, (x, y) = queue.popleft()

        if (x, y) == (X - 1, Y - 1):
            return turn + 1

        for dx, dy in directions:
            nx = dx + x
            ny = dy + y
            if (
                0 <= nx < X
                and 0 <= ny < Y
                and maps[ny][nx] == 1
                and (nx, ny) not in visited
            ):
                queue.append((turn + 1, (nx, ny)))
                visited.add((nx, ny))
    return -1

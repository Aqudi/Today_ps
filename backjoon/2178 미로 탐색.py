import sys
input = sys.stdin.readline
Y, X = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(Y)]
visited = [[0] * X for _ in range(Y)]
result = 0

pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]
queue = [(0, 0, 0)]
while len(queue):
    c, y, x = queue.pop(0)
    if y == Y-1 and x == X-1:
        print(c+1)
        break
    visited[y][x] = 1
    for (offy, offx) in pos:
        _y = y+offy
        _x = x+offx
        if (_y >= 0 and _y < Y) and (_x >= 0 and _x < X) and not visited[_y][_x] and graph[_y][_x]:
            visited[_y][_x] = 1
            queue.append((c+1, _y, _x))

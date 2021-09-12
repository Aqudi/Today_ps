import sys


def updateQueue(field, x, y, invaded, px, py, visited, queue):
    if not visited[y][x][invaded]:
        if field[y][x] == 0:
            visited[y][x][invaded] = visited[py][px][invaded] + 1
            queue.append((x, y, invaded))

        if not invaded and field[y][x] == 1:
            visited[y][x][1] = visited[py][px][invaded] + 1
            queue.append((x, y, True))


Y, X = map(int, sys.stdin.readline().rstrip().split())
field = [list(map(int, list(sys.stdin.readline().strip())))
         for _ in range(Y)]
visited = [[[0, 0] for _ in range(X)] for _ in range(Y)]
queue = [(0, 0, False)]
visited[0][0][0] = 1
answer = sys.maxsize
while len(queue):
    x, y, invaded = queue.pop(0)
    if x == X-1 and y == Y-1:
        answer = visited[y][x][invaded]
        break
    if y > 0:
        updateQueue(field, x, y-1, invaded, x, y, visited, queue)
    if x > 0:
        updateQueue(field, x-1, y, invaded, x, y,  visited, queue)
    if y < Y-1:
        updateQueue(field, x, y+1, invaded, x, y,  visited, queue)
    if x < X-1:
        updateQueue(field, x+1, y, invaded, x, y,  visited, queue)
if answer != sys.maxsize:
    print(answer)
else:
    print(-1)

import sys


def bfs(field, X, Y):
    # 접근 가능한지 확인 (개방된 공기)
    air = [[0 for _ in range(X)] for _ in range(Y)]
    queue = [(0, 0)]
    while len(queue):
        x, y = queue.pop(0)
        air[y][x] = 1
        if x < X-1 and not air[y][x+1] and not field[y][x+1]:
            air[y][x+1] = 1
            queue.append((x+1, y))
        if y < Y-1 and not air[y+1][x] and not field[y+1][x]:
            air[y+1][x] = 1
            queue.append((x, y+1))
        if x > 0 and not air[y][x-1] and not field[y][x-1]:
            air[y][x-1] = 1
            queue.append((x-1, y))
        if y > 0 and not air[y-1][x] and not field[y-1][x]:
            air[y-1][x] = 1
            queue.append((x, y-1))
    return air


def after1H(field, air, X, Y):
    for y in range(1, Y):
        for x in range(X):
            if field[y][x] and (air[y-1][x] + air[y+1][x] + air[y][x-1] + air[y][x+1]) >= 2:
                field[y][x] = 0
    return field


def count(field):
    remain = 0
    for f in field:
        remain += sum(f)
    return remain


Y, X = map(int, sys.stdin.readline().rstrip().split())
field = []
for i in range(Y):
    field.append(list(map(int, sys.stdin.readline().rstrip().split())))
timer = 0
remain = count(field)
while remain != 0:
    air = bfs(field, X, Y)
    field = after1H(field, air, X, Y)
    remain = count(field)
    timer += 1
print(timer)

def find_tomato(s):
    position = []
    for i in range(high):
        for j in range(width):
            if s[i][j] and s[i][j] != -1:
                position.append((i, j))
    return position


def check_around(x, y):
    if x > 0:
        if s[x-1][y] == 0:
            s[x-1][y] = marker
            Que.append((x-1, y))
    if y > 0:
        if s[x][y-1] == 0:
            s[x][y-1] = marker
            Que.append((x, y-1))
    if x < high-1:
        if s[x+1][y] == 0:
            s[x+1][y] = marker
            Que.append((x+1, y))
    if y < width-1:
        if s[x][y+1] == 0:
            s[x][y+1] = marker
            Que.append((x, y+1))


width, high = map(int, input().split())
s = [list(map(int, input().split())) for x in range(high)]

# 토마토의 위치를 기록
Que = find_tomato(s)
# 현재 탐색하고 있는 큐의 위치를 기록
cusor_l = 0
cusor_r = len(Que)-1
# 현재 몇번째 라인을 탐색하고 있는지 기록
before = s[Que[0][0]][Que[0][1]]
while cusor_l <= cusor_r:
    x, y = Que[cusor_l]
    marker = s[x][y] + 1
    check_around(x, y)
    cusor_r = len(Que) - 1
    cusor_l += 1
for i in s:
    if 0 in i:
        marker = 1
# 1은 원래 익어있던 것, 마지막에 marker + 1이 실행된 것 => 빼기 2
print(marker-2)

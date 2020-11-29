def bfs(n, signs, start, end):
    visited = set()
    queue = [start]

    while queue:
        y = queue.pop(0)
        visited.add(y)

        neighbors = signs[y]
        for x in range(n):
            if neighbors[x] == 1:
                if x == end:
                    return 1
                if x not in visited:
                    queue.append(x)
                    visited.add(x)
    return 0


def solution(n, signs):
    answer = [[0 for j in range(n)] for i in range(n)]
    for y in range(n):
        for x in range(n):
            answer[y][x] = bfs(n, signs, y, x)
    return answer


print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
print(solution(3, [[0, 1, 0], [1, 0, 1], [0, 0, 0]]))

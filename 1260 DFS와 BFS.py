N, M, S = map(int, input().split())
edge = [set() for i in range(N + 1)]

for i in range(M):
    u, v = map(int, input().split())
    edge[u].add(v)
    edge[v].add(u)
edge = list(map(lambda x: sorted(list(x)), edge))

def BFS(visited, S):
    queue, result = [S], []
    while len(queue) != 0:
        v = queue.pop(0)
        if visited[v]:
            continue
        visited[v] = True
        result.append(str(v))
        queue.extend(edge[v])
    return result


def DFS(visited, result, s):
    if visited[s]:
        return result
    visited[s] = True
    result.append(str(s))

    for v in edge[s]:
        if visited[v]:
            continue
        result = DFS(visited, result, v)
    return result

visited = [False for i in range(N + 1)]
print(' '.join(DFS(visited, [], S)))
visited = [False for i in range(N + 1)]
print(' '.join(BFS(visited, S)))

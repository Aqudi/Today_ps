V, E = map(int, input().split())
vertex = [[] for i in range(V+1)]
for i in range(E):
    u, v = map(int, input().split())
    vertex[u].append(v)
    vertex[v].append(u)

connected = -1
visited = [False for i in range(V+1)]
queue = [0]
while True:
    while len(queue) != 0:
        v = queue.pop()
        visited[v] = True
        queue.extend([i for i in vertex[v] if visited[i] == False])
    connected += 1
    try:
        queue.append(visited.index(False))
    except ValueError:
        break
print(connected)

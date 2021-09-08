import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
infected = [False for _ in range(N+1)]
graph = {}
for i in range(N):
    graph[i+1] = []
for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)
for k in graph.keys():
    graph[k] = sorted(graph[k])

queue = graph[1]
infected[1] = True
while len(queue) > 0:
    node = queue.pop(0)
    infected[node] = True

    for i in graph[node]:
        if not infected[i]:
            queue.append(i)
        
print(sum(infected)-1)
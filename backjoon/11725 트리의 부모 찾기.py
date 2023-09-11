import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N = int(input())
graph = defaultdict(list)
for i in range(N-1):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = {0: 0}
visited = [0 for i in range(N)]
queue = deque([0])
while queue:
    currentNode = queue.popleft()
    if visited[currentNode]:
        continue
    visited[currentNode] = 1
    for node in graph[currentNode]:
        if node not in parents:
            queue.append(node)
            parents[node] = currentNode

for i in range(1, N):
    print(parents[i] + 1)

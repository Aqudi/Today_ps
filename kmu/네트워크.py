def find(parents, x):
    parent = parents[x]
    if parent == x:
        return x
    parents[x] = find(parents, parent)
    return parents[x]
    
def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        a, b = b, a
    parents[a] = b

def solution(n, computers):
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(parents, i, j)
    for i in range(n):
        parents[i] = find(parents, i)
    return len(set(parents))
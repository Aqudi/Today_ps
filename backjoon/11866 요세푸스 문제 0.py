from collections import deque

N, K = map(int, input().split())
queue = deque(range(N))
answer = "<"
for i in range(N):
    for j in range(K - 1):
        item = queue.popleft()
        queue.append(item)
    answer += f"{queue.popleft()+1}"
    if i != N-1:
        answer += ", "
print(answer + ">")
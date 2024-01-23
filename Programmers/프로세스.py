# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from queue import deque


def solution(priorities, location):
    queue = deque()
    for i, p in enumerate(priorities):
        queue.append((p, i))
    priorities.sort()

    answer = 0
    while queue:
        current = queue.popleft()
        if current[0] == priorities[-1]:
            answer += 1
            priorities.pop()
            if current[1] == location:
                break
        else:
            queue.append(current)
    return answer

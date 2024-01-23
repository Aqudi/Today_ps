# https://school.programmers.co.kr/learn/courses/30/lessons/87946
# BFS, 완전탐색
from itertools import permutations


def solution(k, dungeons):
    length = len(dungeons)
    routes = permutations(range(length), length)

    answer = -1
    for route in routes:
        count = 0
        currentK = k
        for step in route:
            minK, cost = dungeons[step]
            if currentK >= minK:
                currentK -= cost
                count += 1
            else:
                break

        answer = max(answer, count)
        if answer == length:
            break

    return answer

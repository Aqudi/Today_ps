# https://school.programmers.co.kr/learn/courses/30/lessons/42576
from collections import defaultdict


def solution(participant, completion):
    completionMap = defaultdict(int)

    for name in completion:
        completionMap[name] += 1
    for name in participant:
        completionMap[name] -= 1
        if completionMap[name] < 0:
            return name

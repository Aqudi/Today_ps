# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# n이 최대 100개로 굉장히 작음 => 완전탐색 가능~ wire를 하나씩 끊어보면서 확인
# Union-find 수행 후 마지막에 최종적인 부모를 탐색하는 과정이 빠져서 헤맸음...
import sys
from collections import Counter


def find(parents, node):
    if parents[node] == node:
        return node
    parent = find(parents, parents[node])
    parents[node] = parent
    return parent

def union(parents, node1, node2):
    parent1 = find(parents, node1)
    parent2 = find(parents, node2)
    if parent1 > parent2:
        parents[parent1] = parent2
    else:
        parents[parent2] = parent1

def solution(n, wires):
    answer = sys.maxsize
    for i in range(len(wires)):
        # 자르기
        modified_wires = wires[:i] + wires[i+1:]
        
        # union find
        parents = {i:i for i in range(1, n+1)}
        for w in modified_wires:
            union(parents, w[0], w[1])
            
        # 연결 요소내의 정점 개수 구하기
        for node in range(1, n+1):
            find(parents, node)  # 각 노드에 대한 최종 부모 찾기
        counts = Counter(parents.values())
        sub_count1 = counts[find(parents, wires[i][0])]
        sub_count2 = counts[find(parents, wires[i][1])]
        answer = min(answer, abs(sub_count1 - sub_count2))
    return answer
"""
알고리즘의 복잡도가 정렬 O(NlogN * (N-1)) = O(N^2 log N) 이었음
가장 큰 영향을 미치는 부분은 loop 속에 cards sort 부분

이 부분을 heapq와 같은 다른 데이터 구조로 변환함으로써 문제를 해결할 수 있었음
"""
import sys

input = sys.stdin.readline
N = int(input())
cards = [int(input()) for _ in range(N)]
answer = 0
while len(cards) != 1:
    cards.sort()
    t = cards.pop(0) + cards.pop(0)
    answer += t
    cards.append(t)
print(answer)

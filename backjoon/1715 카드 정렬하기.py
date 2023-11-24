import sys
import heapq

input = sys.stdin.readline
N = int(input())
cards = [int(input()) for _ in range(N)]
answer = 0
heapq.heapify(cards) # O(N) # list sort O(N log N) 알고리즘을 heap queue로 변환
while len(cards) != 1:
    t = heapq.heappop(cards) + heapq.heappop(cards)  # O(log N)
    heapq.heappush(cards, t)
    answer += t
print(answer)

import sys
import heapq

input = sys.stdin.readline
N, K = list(map(int, input().split()))
# 보석 (무게, 가치) 리스트 - 무게 순으로 정렬
gems = sorted(
    [tuple(map(int, input().split())) for _ in range(N)],
    key=lambda x: x[0],
    reverse=True,
)
# 가방 무게 제한 리스트
bags = sorted([int(input()) for _ in range(K)])

answer = 0
candidateGemValues = []
for bag in bags:
    while gems and bag >= gems[-1][0]:
        _, value = gems.pop()
        # 현재 가방에 넣을 수 있는 높은 가치 순으로 정렬
        heapq.heappush(candidateGemValues, -value)
    if candidateGemValues:
        # 이전 가방은 현재 가방보다 제한이 낮았으므로
        # 이전 가방에 넣을 수 있는 보석은 현재 가방에도 넣을 수 있음
        answer += -1 * heapq.heappop(candidateGemValues)
print(answer)

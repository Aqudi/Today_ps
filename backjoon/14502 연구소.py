from collections import deque
from itertools import combinations
import copy
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
blanks = []
viruses = []
answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blanks.append((i, j))
        elif board[i][j] == 2:
            viruses.append((i, j))
safeAreas = len(blanks) - 3

# 벽을 세울 때 중복되는 조합을 없애기 위해서 조합을 사용
# 예시) (1,1), (2,2), (3,3)과 (2,2), (1,1), (3,3)은 같은 조합
wallCombinations = combinations(blanks, 3)


def simulate(simBoard):
    """BFS로 바이러스 퍼트리고 점수 계산해서 업데이트"""
    # 바이러스 퍼트리기
    queue = deque(viruses)
    infected = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            nextY = y + dy
            nextX = x + dx
            if 0 <= nextY < N and 0 <= nextX < M:
                if simBoard[nextY][nextX] == 0:
                    infected += 1
                    simBoard[nextY][nextX] = 2
                    queue.append((nextY, nextX))
    # 점수계산
    global answer
    answer = max(answer, safeAreas - infected)


def solve():
    """벽 3개 세우고 바이러스 퍼트리기"""
    for wallCombination in wallCombinations:
        simBoard = copy.deepcopy(board)
        for i, j in wallCombination:
            simBoard[i][j] = 1
        simulate(simBoard)
    print(answer)


solve()

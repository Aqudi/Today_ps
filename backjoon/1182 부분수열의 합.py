import sys
N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
visited = [0 for i in range(N)]
answer = 0


def dfs(start, csum):
    global answer
    # 정답 조건 & 시작했을 때는 csum업데이트가 안된 상태
    if csum == S and start != 0:
        answer += 1

    for next in range(start, N):
        # 방문한(수열에 포함된)노드는 재방문 X
        if visited[next]:
            continue

        # 방문 & 수열길이 + 1
        visited[next] = True
        csum += nums[next]
        dfs(next+1, csum)

        # 백트래킹 & 수열길이 - 1
        visited[next] = False
        csum -= nums[next]


dfs(0, 0)
print(answer)

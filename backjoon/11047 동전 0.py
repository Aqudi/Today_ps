# 동전의 가치가 이전 동전의 배수로 표현됨
# 그러므로 그리디 접근법으로 해결했을 때 부분합이 최적의 값임을 보장할 수 있음
N, K = map(int, input().split())
coins = []
for i in range(N):
    coins.insert(0, int(input()))
answer = 0
for coin in coins:
    count = K // coin
    K -= count * coin
    answer += count
    if K == 0:
        break
print(answer)
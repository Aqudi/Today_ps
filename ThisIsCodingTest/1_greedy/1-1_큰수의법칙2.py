N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
answer = 0
k = K
while M > 0:
    answer += nums[k == 0]
    k-=1
    M-=1
    if k == 0:
        k = K
print(answer)
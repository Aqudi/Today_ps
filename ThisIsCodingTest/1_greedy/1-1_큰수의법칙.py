N, M, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
n1, n2 = nums[:2]
n2Count = int(M / (K+1))
n1Count = K - n2Count
answer = n1Count * n1 + n2Count * n2
print(answer)
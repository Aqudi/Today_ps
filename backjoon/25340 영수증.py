X = int(input())
N = int(input())
nums = [tuple(map(int, input().split())) for _ in range(N)]
total = 0
for a, b in nums:
    total += a * b
print("Yes" if total == X else "No")
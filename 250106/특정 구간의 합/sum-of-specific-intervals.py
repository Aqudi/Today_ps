n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!
for (start, end) in queries:
    print(sum(arr[start-1:end]))
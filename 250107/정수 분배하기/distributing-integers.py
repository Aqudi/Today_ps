n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Write your code here!
left = 1
right = max(arr)
result = 0

while left <= right:
    mid = (left + right) // 2

    count = 0
    for number in arr:
        while number - mid >= 0:
            count += 1
            number -= mid
        
    if count >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
        
s = int(input())

# Write your code here!
left = 1
right = s
max_num = 0

while left <= right:
    mid = (left + right) // 2

    if mid * (mid+1) // 2 <= s:
        left = mid+1
        max_num = max(mid, max_num)
    else:
        right = mid -1

print(max_num)
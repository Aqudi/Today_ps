n = int(input())
k = int(input())

answer = n * n
left = 0
right = n * n
while left <= right:
    mid = (left+ right) // 2
    
    count = 0
    for i in range(1, n+1):
        # i행에는 i의 배수들이 있으니 최대 n개 또는 mid 이하의 i의 배수 수 만큼 존재
        count += min(n, mid // i) 

    if count >= k:
        right = mid -1
        answer = min(mid, answer)
    else:
        left = mid + 1

print(answer)

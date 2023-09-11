N = int(input())
k = 1
answer = 0
while N > 0:
    if N < k:
        k = 1
    N -= k
    k += 1
    answer += 1
print(answer)
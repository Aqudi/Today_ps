N = int(input())
answer = 0
for i in range(N):
    # 분해합 계산
    digitSum = i + sum(map(int, str(i)))
    if N == digitSum:
        answer = i
        break
print(answer)

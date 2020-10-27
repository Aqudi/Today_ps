# DP문제
# 중요한 포인트 : 규칙 찾기 -> 점화식 만들기
# 타일을 붙이는 방법 : 길이 1(1*2 한 개), 길이 2추가(2*1 두 개)

num = int(input())
memo = [0 for i in range(num + 1)]
for i in range(1, num+1):
    if i == 1:
        memo[i] = 1
    elif i == 2:
        memo[i] = 2
    else:      
        memo[i] = (memo[i-1] + memo[i-2]) % 10007
print(memo[-1] % 10007)
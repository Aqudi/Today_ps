def is_prime_number(x):
    # 1이 아니면서 2부터 (x-1)까지의 수로 나누어 떨어지지 않는 수
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


N = int(input())
nums = list(map(int, input().split()))
answer = 0
for n in nums:
    if is_prime_number(n):
        answer += 1
print(answer)

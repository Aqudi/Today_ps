# 활용해야하는 개념들
# 소수 구하기 M * M >= M * N (단, M >= N)
# 오일러 피 함수 (n보다 작고 서로수인 k 개수 구하기)

def factorize(n, root):
    nums = set()
    factor = 2
    while factor <= root:
        if factor and n % factor == 0:
            nums.add(factor)
            n /= factor
        else:
            factor += 1
    if n != 1:
        nums.add(int(n))
    return nums


N = int(input())
factors = factorize(N, int(N ** 0.5 + 1))
answer = N
for f in factors:
    answer *= (f-1) / f
print(int(answer))

# 2번 시도 (시간초과)
# def factorize(n):
#     nums = set()
#     factor = 2
#     while factor <= n:
#         if factor and n % factor == 0:
#             nums.add(factor)
#             n /= factor
#         else:
#             factor += 1
#     return nums


# N = int(input())
# factors = factorize(N)
# answer = N
# for f in factors:
#     answer *= (f-1) / f
# print(int(answer))

# 1번 시도 (시간초과)
# def gcd(a, b):
#     if a < b:
#         a, b = b, a
#     while b != 0:
#         mod = a % b
#         a = b
#         b = mod
#     return a
# def phi(n):
#     count = 0
#     for i in range(1, n+1):
#         if gcd(n, i) == 1:
#             count += 1
#     return count

# print(phi(int(input())))

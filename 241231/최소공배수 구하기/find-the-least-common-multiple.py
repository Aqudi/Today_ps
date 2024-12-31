n, m = map(int, input().split())

def gcd(a, b):
    remain = a % b
    if remain == 0:
        return b
    return gcd(a, r)


print(n * m // gcd(max(n, m), min(n, m)))
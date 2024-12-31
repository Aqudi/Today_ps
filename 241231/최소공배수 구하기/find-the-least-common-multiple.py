n, m = map(int, input().split())

def gcd(a, b):
    remain = max(a, b) % min(a, b)
    if remain == 0:
        return min(a, b)
    return remain

print(n * m // gcd(n, m))
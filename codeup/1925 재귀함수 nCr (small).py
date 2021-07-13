def factorial(n):
    if n <= 2:
        return n
    return factorial(n-1) * n


n, r = map(int, input().split())
print(factorial(n) // (factorial(r) * factorial(n-r)))

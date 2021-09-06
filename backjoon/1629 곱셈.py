def pow(a, b, c):
    result = 1
    while b:
        if b % 2 == 1:
            result = result * a % c
        a = a * a % c
        b //= 2
    return result


A, B, C = map(int, input().split())
print(pow(A, B, C) % C)

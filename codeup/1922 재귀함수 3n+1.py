def recursive_3n1(n, i=1):
    if n == 1:
        return i
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n // 2
    return recursive_3n1(n, i+1)


print(recursive_3n1(int(input())))

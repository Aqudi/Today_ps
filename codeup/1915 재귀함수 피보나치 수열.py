def recursive_fibo(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    return recursive_fibo(n-1) + recursive_fibo(n-2)

n = int(input())
print(recursive_fibo(n-1))
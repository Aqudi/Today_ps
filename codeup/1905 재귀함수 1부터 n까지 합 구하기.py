import sys
sys.setrecursionlimit(1000000)


def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n-1)


n = int(input())
print(recursive_sum(n))

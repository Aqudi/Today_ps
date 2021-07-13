def print_star(n):
    if n == 0:
        return
    print('*', end='')
    print_star(n-1)


def print_line(n, i):
    if i > n:
        return
    print_star(i)
    print()
    print_line(n, i+1)


n = int(input())
print_line(n, 1)

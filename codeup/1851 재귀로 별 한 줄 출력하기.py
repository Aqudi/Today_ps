def print_star(n):
    if n == 0:
        return
    print('*', end='')
    print_star(n-1)


n = int(input())
print_star(n)
def print_odd_number(a, b, i):
    if a == i:
        if a % 2 == 0:
            i += 1

    if (i == b and b % 2 == 0) or i > b:
        return
    print(i, end=' ')
    print_odd_number(a, b, i+2)


a, b = map(int, input().split(' '))
print_odd_number(a, b, a)

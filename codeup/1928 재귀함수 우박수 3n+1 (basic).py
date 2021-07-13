def woo_park_su(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n = n // 2

    woo_park_su(n)


woo_park_su(int(input()))

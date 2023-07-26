def polynomial_addition(t1, t2):
    t3 = [[], []]
    pointer_a = 0
    pointer_b = 0
    while pointer_a < len(t1[1]) and pointer_b < len(t2[1]):
        expon_a = t1[1][pointer_a]
        expon_b = t2[1][pointer_b]
        coeffi_a = t1[0][pointer_a]
        coeffi_b = t2[0][pointer_b]
        if expon_a < expon_b:
            attach(t3, coeffi_b, expon_b)
            pointer_b += 1

        elif expon_a == expon_b:
            attach(t3, coeffi_a+coeffi_b, expon_a)
            pointer_a += 1
            pointer_b += 1

        elif expon_a > expon_b:
            attach(t3, coeffi_a, expon_a)
            pointer_a += 1

    for i in range(pointer_a, len(t1[0])):
        attach(t3, t1[0][pointer_a], t1[1][pointer_a])
        pointer_a += 1

    for i in range(pointer_b, len(t1[0])):
        attach(t3, t2[0][pointer_b], t2[1][pointer_b])
        pointer_b += 1

    return t3


def attach(t, coeffi, expon):
    if coeffi:
        t[0].append(coeffi)
        t[1].append(expon)


test1 = [[3, 5, 6, 4],
         [4, 2, 1, 0]]
test2 = [[5, 4, -6, 1],
         [3, 2, 1, 0]]
result = polynomial_addition(test1, test2)
print(result)

result = polynomial_addition(test2, test1)
print(result)

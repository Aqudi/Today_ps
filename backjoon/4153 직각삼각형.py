l1, l2, l3 = sorted(map(int, input().split()))
while l1 != 0 and l2 != 0 and l3 != 0:
    if l3**2 == l1**2 + l2**2:
        print("right")
    else:
        print("wrong")
    l1, l2, l3 = sorted(map(int, input().split()))

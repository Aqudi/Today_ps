P = input()
while P != "0":
    length = len(P)
    first = P[:length//2]
    last = None
    if length % 2 == 1:
        last = ''.join(reversed(P[length//2+1:]))
    else:
        last = ''.join(reversed(P[length//2:]))
    if first == last:
        print("yes")
    else:
        print("no")
    P = input()

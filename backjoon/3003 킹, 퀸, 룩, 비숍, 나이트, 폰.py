exists = list(map(int, input().split()))
expected = [1, 1, 2, 2, 2, 8]
for i in range(len(exists)):
    print(expected[i] - exists[i], end=" ")

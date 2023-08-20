N = int(input())
floor = 1
current = 1
while N > current:
    current += floor * 6
    floor += 1
print(floor)

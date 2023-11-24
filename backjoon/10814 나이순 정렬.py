import sys

input = sys.stdin.readline
N = int(input())
ageAndName = [tuple(input().split()) for i in range(N)]
ageAndName.sort(key=lambda x: int(x[0]))
for age, name in ageAndName:
    print(age, name)

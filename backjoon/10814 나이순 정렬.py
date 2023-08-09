N = int(input())
ageAndName = [tuple(input().split()) for i in range(N)]
ageAndName.sort(key=lambda x: x[1])
ageAndName.sort(key=lambda x: x[0])
for age, name in ageAndName:
    print(age, name)

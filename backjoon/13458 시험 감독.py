N = int(input())
rooms = map(int, input().split())
B, C = map(int, input().split())
answer = 0
for room in rooms:
    forSub = room - B
    supervisors = 1
    if forSub > 0:
        supervisors = forSub // C + 1
        if forSub % C != 0:
            supervisors += 1
    answer += supervisors
print(answer)

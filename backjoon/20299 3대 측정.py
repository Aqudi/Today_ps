import sys
input = sys.stdin.readline
N, K, L = map(int, input().split())
teams = []
for i in range(N):
    members = list(map(int, input().split()))
    if K <= sum(members) and L <= min(members):
        teams.append(members)
print(len(teams))
print(' '.join(map(lambda x: f"{x[0]} {x[1]} {x[2]}", teams)))

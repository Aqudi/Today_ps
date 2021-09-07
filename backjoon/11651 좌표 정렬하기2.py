import sys
N = int(sys.stdin.readline().rstrip())
ps = []
for i in range(N):
    ps.append(list(map(int, sys.stdin.readline().rstrip().split())))

ps = sorted(ps, key=lambda x: x[0])
ps = sorted(ps, key=lambda x: x[1])

for p in ps:
    print(p[0], p[1]) 

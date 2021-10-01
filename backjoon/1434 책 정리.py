import sys
input = sys.stdin.readline
N, M = map(int, input().split())
boxes = list(map(int, input().split()))
books = list(map(int, input().split()))
cbook, cbox = 0, 0
while cbook < M:
    if boxes[cbox] >= books[cbook]:
        boxes[cbox] -= books[cbook]
        cbook += 1
    else:
        cbox += 1
print(sum(boxes))

import sys

input = sys.stdin.readline
N = int(input())
queue = []
for i in range(N):
    cmd = input().split()
    value = cmd[-1]
    cmd = cmd[0]
    if cmd == "push_back":
        queue.append(value)
    elif cmd == "push_front":
        queue.insert(0, value)
    elif cmd == "front" or cmd == "back" or "pop" in cmd:
        if len(queue) == 0:
            print(-1)
        elif cmd == "pop_front":
            print(queue.pop(0))
        elif cmd == "pop_back":
            print(queue.pop())
        elif cmd == "front":
            print(queue[0])
        elif cmd == "back":
            print(queue[-1])
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if queue else 1)

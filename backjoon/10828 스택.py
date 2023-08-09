from collections import deque
import sys

queue = deque()
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    value = cmd[-1]
    cmd = cmd[0]
    queueSize = len(queue)
    if cmd == "push":
        queue.append(value)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(1 if len(queue) == 0 else 0)
    elif len(queue) != 0:
        if cmd == "pop":
            print(queue.pop())
        elif cmd == "top":
            print(queue[-1])
    else:
        print(-1)

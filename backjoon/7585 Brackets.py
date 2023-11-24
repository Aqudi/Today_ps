import sys

stack = []
brackets = {}
for start, end in zip("({[", ")}]"):
    brackets[start] = end
    brackets[end] = start

while True:
    stack.clear()
    code = sys.stdin.readline().rstrip()
    if code == "#":
        break
    result = True
    for s in code:
        if s in "({[":
            stack.append(s)
        if s in ")}]":
            if len(stack) == 0:
                result = False
                break
            if stack[-1] != brackets[s]:
                result = False
                break
            stack.pop()
    print("Legal" if result and len(stack) == 0 else "Illegal")

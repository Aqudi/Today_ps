import sys

input = sys.stdin.readline
str = ""

while True:
    str = input().rstrip()
    if str == ".":
        break
    stack = list()
    try:
        for s in str:
            if s in "([":
                stack.append(s)
            if s in ")]":
                if s == ")" and stack[-1] == "(":
                    stack.pop()
                elif s == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    # 닫는 괄호의 짝이 stack의 최상단에 없다면 "no"
                    break
        if not stack:
            # 닫는 괄호의 짝이 stack의 최상단에 없다면 "no"
            print("yes")
            continue
    except:
        pass

    # 모든 문자열을 순회했을 때도 stack이 비지 않은 상태일 때
    # 또는 닫는 괄호가 나왔지만 stack이 빈 상태일 때 "no"
    print("no")

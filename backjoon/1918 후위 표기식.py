M = {
    "(": 0,
    ")": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


def solve(fom: str, recursive=False):
    stack = []
    answer = ""
    i = 0

    while i < len(fom):
        # 괄호 처리
        if fom[i] == "(":
            stack.append(fom[i])
        elif fom[i] == ")":
            # 여는 괄호가 나올 때까지 답에 추가한다.
            pop = stack.pop()
            while len(stack) > 0 and pop != "(":
                answer += pop
                pop = stack.pop()

        # 일반 연산자나 숫자일 경우
        elif fom[i] in M.keys():
            # 자신보다 높은 우선순위가 스택내에 있다면 답에 추가한다.
            while len(stack) > 0 and (M[fom[i]] <= M[stack[-1]]):
                answer += stack.pop()
            # 연산자 스택에 연산자를 쌓는다.
            stack.append(fom[i])
        else:
            # 숫자는 바로 답에 추가한다.
            answer += fom[i]
        i += 1

    # 남은 연산자를 모두 답에 추가한다.
    for i in range(len(stack)):
        answer += stack.pop()
    return answer


print(solve(input()))

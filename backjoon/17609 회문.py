import sys

input = sys.stdin.readline
N = int(input())
strs = (input().rstrip() for _ in range(N))


def check(s, removeAt=None):
    """문자열 s에서 removeAt에 위치한 문자를 제거한 문자열이 회문인지 검사"""
    length = len(s)
    if removeAt != None:
        # removeAt에 위치한 문자 제거
        left = s[:removeAt]
        right = s[removeAt + 1 :] if removeAt < len(s) else len(s) - 1
        s = left + right
        length = len(s)

    # 회문 검사
    failedAt = None
    mid = (length // 2 - 1) + 1
    for i1 in range(mid):
        i2 = -1 * i1 - 1
        char1 = s[i1]
        char2 = s[i2]
        if char1 != char2:
            failedAt = i1
            break
    return failedAt


for s in strs:
    failedAt = check(s)
    if failedAt != None:
        if check(s, failedAt) != None:
            failedAt = len(s) + (-1 * failedAt - 1)
            if check(s, failedAt) != None:
                # 회문이 아님
                print(2)
                continue
        # 유사회문임
        print(1)
        continue
    else:
        # 회문
        print(0)
        continue

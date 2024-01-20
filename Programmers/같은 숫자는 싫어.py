# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    last = None
    answer = []
    for a in arr:
        if last != a:
            answer.append(a)
        last = a
    return answer

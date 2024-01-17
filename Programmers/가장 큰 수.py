# https://school.programmers.co.kr/learn/courses/30/lessons/42746#
# functools.cmp_to_key 함수로도 유사한 동작을 구현할 수 있음

class MyNumber:
    def __init__(self, number):
        self.number = str(number)

    def __lt__(self, other):
        return self.number + str(other) < str(other) + self.number

    def __str__(self):
        return self.number


def solution(numbers):
    numbers = list(map(MyNumber, numbers))
    numbers.sort(reverse=True)
    start = 0
    for n in numbers[:-1]:
        if str(n) == "0":
            start += 1
        else:
            break
    return "".join(map(str, numbers[start:]))

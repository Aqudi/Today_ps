import sys


input = sys.stdin.readline
N = int(input())
# generator를 통해서 리스트를 메모리에 두지 않고 nums 입력
nums = (int(input()) for _ in range(N))

# 문제 조건을 참고하여 counts 리스트 선언
counts = [0] * 10001
for n in nums:
    counts[n] += 1

# counting sort
for i, count in enumerate(counts):
    while count:
        print(i)
        count -= 1

M, N = map(int, input().split())


# 에라토스테네스의 체
def solve():
    maxNum = N + 1
    nums = [0, 0] + [i for i in range(2, maxNum)]

    # 2부터 시작해서 특정 수의 배수에 해당하는 수를 모두 지움
    # 자기 자신을 제외하고, 이미 지워진 수는 건너뜀
    for i in range(2, maxNum):
        if nums[i] == 0:
            continue

        # 지워진 숫자가 아니라면 그 배수부터 시작해서 배수들을 지움
        for j in range(2 * i, maxNum, i):
            nums[j] = 0

    for num in nums[M:]:
        if num != 0:
            print(num)


solve()

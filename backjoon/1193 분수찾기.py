"""
개수 방향 분수리스트
1개  ->  1/1
2개  <-  2/1 1/2
3개  ->  3/1 2/2 1/3
...
"""

N = int(input())
pos = None  # (row, col)
count = 0
i = 0
for i in range(1, N + 1):
    count += i
    if count >= N:
        pos = (i, N - count + i - 1)
        break

lineNums = list(range(1, pos[0] + 1))
nums = (lineNums[pos[1]], list(reversed(lineNums))[pos[1]])
if pos[0] % 2 == 1:
    print(f"{nums[1]}/{nums[0]}")
else:
    print(f"{nums[0]}/{nums[1]}")

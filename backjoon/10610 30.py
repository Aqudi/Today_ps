N = input()
nums = sorted(list(map(int, N)), reverse=True)
result = int("".join(map(str, nums)))
if result % 30 == 0:
    print(result)
else: 
    print(-1)

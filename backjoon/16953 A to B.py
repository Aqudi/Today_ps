A, B = map(int, input().split())
queue = [(A, 1)]
answer = -1
while len(queue):
    num, count = queue.pop(0)
    mul2 = num * 2
    plus1 = int(f"{str(num)}1")
    if mul2 == B or plus1 == B:
        answer = count + 1
        break
    if mul2 < B:
        queue.append((mul2, count+1))
    if plus1 < B:
        queue.append((plus1, count+1))
print(answer)

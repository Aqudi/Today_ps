T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    rank = sorted(queue, reverse=True)

    answer = 0
    r = rank.pop(0)
    while queue:
        q = queue.pop(0)
        if q == r:
            answer += 1
            if M == 0:
                break
            r = rank.pop(0)
        else:
            queue.append(q)

        M -= 1
        if M < 0:
            M = len(queue) - 1
    print(answer)

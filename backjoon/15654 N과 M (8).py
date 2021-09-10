def pop(x):
    return x.pop() if len(x) else None

def solve(numbers, history, step, N, M):
    for i in range(history[-1], N+1):
        if step <= 1:
            if  len(history) == M:
                converted = [numbers[idx] for idx in history]
                print(' '.join(map(str, converted)))
                pop(history)
                history.append(i+1)
        else:
            history.append(i)
            if step > 0:
                solve(numbers, history, step-1, N, M)
            pop(history)
        pop(history)
        history.append(i+1)


N, M = map(int, input().split())
numbers = [0] + sorted(list(map(int, input().split())))
solve(numbers, [1], M, N, M)
def pop(x):
    return x.pop() if len(x) else None

def solve(ns, step, N, M):
    for i in range(ns[-1], N+1):
        if step <= 1:
            if  len(ns) == M:
                print(' '.join(map(str, ns)))
                pop(ns)
                ns.append(i+1)
        else:
            ns.append(i)
            if step > 0:
                solve(ns, step-1, N, M)
            pop(ns)
        pop(ns)
        ns.append(i+1)


N, M = map(int, input().split())
solve([1], M, N, M)
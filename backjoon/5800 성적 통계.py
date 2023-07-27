def gap(l):
    result = []
    for i in range(len(l) - 1):
        result.append(l[i] - l[i + 1])
    return result


n = int(input())
for i in range(n):
    scores = list(map(int, input().split()))
    student = scores[0]
    scores = sorted(scores[1:], reverse=True)
    gaps = gap(scores)

    print("Class", i+1)
    print(f"Max {max(scores)}, Min {min(scores)}, Largest gap {max(gaps)}")
    
candidates = '0123456789ABCDEF'


def convert_base(n, k):
    if n < k:
        return candidates[n]

    return f"{convert_base(n//k, k)}{candidates[n%k]}"


n, k = map(int, input().split())
print(convert_base(n, k))

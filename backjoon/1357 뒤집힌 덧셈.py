def reversedInt(x): return int(''.join(list(reversed(str(x)))))
a, b = input().split()
print(reversedInt(reversedInt(a) + reversedInt(b)))

N = int(input())
words = list(set([input() for i in range(N)]))
words.sort()
words.sort(key=lambda x: len(x))
for w in words:
    print(w)

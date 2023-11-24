import sys

for text in sys.stdin:
    a, b = map(int, text.split())
    print(a + b)

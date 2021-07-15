N = int(input())
s = ''
n = N
while n >= 1:
    s = f'{n%2}{s}'
    n //= 2
print(s)

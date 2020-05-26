a,b = map(int, sorted(input().split()))
L = a*b
while b!=0:
    a,b = b, a%b
print(f"{a}\n{L//a}")
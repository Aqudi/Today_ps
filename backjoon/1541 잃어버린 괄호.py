ex = input()
subs = []
sub = ""
for e in ex:
    if e == "-":
        subs.append(sum(map(int, sub.split("+"))))
        sub = ""
    else:
        sub +=  e
subs.append(sum(map(int, sub.split("+"))))
answer = subs[0]
for s in subs[1:]:
    answer -= s
print(answer)

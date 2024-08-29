D = [0]
D[0], p = map(str, input().split())
ans = 0

while 1:
    newNum = 0
    for s in D[-1]:
        newNum += int(s) ** int(p)
    if str(newNum) not in D:
        D.append(str(newNum))
        continue
    ans = D.index(str(newNum))
    break

print(ans)
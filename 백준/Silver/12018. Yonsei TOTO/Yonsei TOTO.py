n, m = map(int, input().split())
arr = [() for _ in range(n)]
for i in range(n):
    p, l = map(int, input().split())
    arr[i] = (l,sorted(list(map(int, input().split())), reverse=True))

temp = []

for j in range(n):
    peoples = arr[j][0]
    table = arr[j][1]
    if len(table) < peoples:
        temp.append(1)
    else:
        temp.append(table[peoples-1])

temp = sorted(temp)
total = count = 0
for people in temp:
    total += people
    if total > m:
        break
    count += 1
print(count)
from sys import stdin
input = stdin.readline

n = int(input())
stack = []
count = 1
ans = []
flag = 1

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        ans.append("+")
        count += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        flag = 0
        break

if flag:
    print(*ans)
else:
    print("NO")
N = int(input())
tower = list(map(int, input().split()))

ans = [0] * N
stack = []

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i,tower[i]))
        
print(*ans)
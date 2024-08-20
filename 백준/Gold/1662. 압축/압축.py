import sys
input = sys.stdin.readline

S = input().rstrip()
ans = 0
stack = []
for s in S:
    if s == '(':
        stack.append([int(tmp), ans-1])
        ans = 0
    elif s == ')':
        k, prev = stack.pop()
        ans = k*ans+prev
    else:
        tmp = s
        ans += 1
print(ans)
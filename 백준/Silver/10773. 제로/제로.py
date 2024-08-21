from sys import stdin
input = stdin.readline

k = int(input())
stack = []
for _ in range(k):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

if len(stack) == 0:
    stack.append(0)
    
print(sum(stack))
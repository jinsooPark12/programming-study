import sys
input = sys.stdin.readline

N = int(input())
target = -1
s = []
for _ in range(N):
    key = input().rstrip()
    if key == "top":
        if len(s) == 0:
            print(-1)
            continue
        print(s[len(s)-1])
    elif key == "pop":
        if len(s) == 0:
            print(-1)
            continue
        print(s.pop())
    elif key == "size":
        print(len(s))
    elif key == "empty":
        if len(s) == 0:
            print(1)
            continue
        print(0)
    else:
        k, item = key.split()
        s.append(item)
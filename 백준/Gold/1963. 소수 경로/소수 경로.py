from collections import deque
import sys
input = sys.stdin.readline

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0:
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return arr

def dfs(s, e):
    count = 0
    dx = [1,10,100,1000]
    q = deque()
    q.append((s,count))
    visited.append(s)
    
    while q:
        num, c = q.popleft()
        
        if num == e:
            return c
        
        for i in range(4):
            temp = num
            a = (temp // dx[i]) % 10
            temp -= a*dx[i]
            for j in range(0, 10):
                t = (temp+(j*dx[i]))
                if t >= 1000:
                    if sosu[t] and t not in visited:
                        visited.append(t)
                        q.append((t, c + 1))
    return -1

sosu = prime_numbers(10000)

T = int(input())
for _ in range(T):
    visited = []
    start, end = map(int, input().split())
    ans = dfs(start, end)
    if ans == -1:
        print("Impossible")
    else:
        print(ans)
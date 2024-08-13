from collections import deque

def bfs(a,b):
    visited = [0 for _ in range(n+1)]
    count = 0
    q = deque()
    q.append((a, count))
    visited[a] = 1
    
    while q:
        node, cur = q.popleft()
        
        if b in trees[node]:
            if cur == 0:
                return trees[node][b]
            return cur + trees[node][b]
        
        for key in trees[node]:
            if visited[key] == 0:
                visited[key] = 1
                q.append((key, cur + trees[node][key]))   

n, m = map(int, input().split())

trees = [{} for _ in range(n+1)]

for _ in range(n-1):
    s, e, c = map(int, input().split())
    trees[s][e] = c
    trees[e][s] = c


for _ in range(m):
    n1, n2 = map(int, input().split())
    print(bfs(n1, n2))
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 1
    q = deque()
    q.append((a,b))
    matrix[a][b] = 0
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                count += 1
                q.append((nx,ny))
                
    return count
    
n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            cnt += 1
            ans = max(ans, bfs(i,j))
            
print(cnt)
print(ans)
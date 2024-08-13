from collections import deque
# 조건1 - 단지(연결되어 있는 1)의 개수 확인
# 조건2 - 단지의 크기 확인
def bfs(a, b):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 0
    visited[a][b] = 1
    queue = deque()
    queue.append((a,b))
    min_y, max_y = b,b
    
    while queue:
        x,y = queue.popleft()
        count += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx,ny))
                
    ans.append(count)

n = int(input())
matrix = []
visited = [[0 for _ in range(n)] for _ in range(n)]
ans = []

for _ in range(n):
    matrix.append(list(map(int, input())))
    
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and matrix[i][j] == 1:
            bfs(i, j)
            
ans.sort()
print(len(ans))
for k in range(len(ans)):
    print(ans[k])
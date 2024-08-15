from collections import deque
def bfs(a,b):
    count = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((a,b,count))
    visited[a][b] = 1
    
    while q:
        x,y,c = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                c += 1
                visited[nx][ny] = 1
                q.append((nx,ny,c))
    answer.append(c)

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    matrix = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    answer = []
    for _ in range(k):
        X,Y = map(int, input().split())
        matrix[Y][X] = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
    print(len(answer))
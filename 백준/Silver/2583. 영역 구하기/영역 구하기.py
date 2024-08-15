from collections import deque

def bfs(a,b):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 1
    
    q = deque()
    q.append((a,b))
    matrix[a][b] = 1
    
    while q:
        x,y= q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                q.append((nx,ny))
                count += 1
    answer.append(count)

m, n, k = map(int, input().split())
matrix = [[0]*m for _ in range(n)]
answer = []

for _ in range(k):
    x1, y1, x2, y2 = map(int,input().split())
    length_x = x2 - x1
    length_y = y2 - y1

    for i in range(length_x):
        for j in range(length_y):
            matrix[x1+i][y1+j] = 1

# for i in range(n):
#     print(matrix[i])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            bfs(i,j)

answer.sort()
print(len(answer))
print(*answer)
from collections import deque

def bfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            
            if ddx < 0 or ddx >= N or ddy < 0 or ddy >= M:
                continue
            if matrix[ddx][ddy] == 0:
                continue
            if matrix[ddx][ddy] == 1:
                matrix[ddx][ddy] = matrix[x][y]+1
                queue.append((ddx,ddy))
    
    return matrix[N-1][M-1]

N, M = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input())))

print(bfs(0,0))
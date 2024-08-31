# 각 껍질별로 1차원 배열로 나열
from collections import deque

n, m, r = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
ans = [[0]*m for _ in range(n)]
table = deque()

loops = min(n,m) // 2    # 행과 열 중 작은 쪽의 절반만큼 겹이 쌓임
for i in range(loops):
    table.clear()
    table.extend(matrix[i][i:m-i])  # 위
    table.extend([row[m-i-1] for row in matrix[i+1:n-i-1]]) # 오른쪽
    table.extend(matrix[n-i-1][i:m-i][::-1])    # 아래
    table.extend(row[i] for row in matrix[i+1:n-i-1][::-1]) # 왼쪽
    
    table.rotate(-r)    # r만큼 왼쪽으로 회전
    
    # 생성된 데크의 맨 처음 수를 하나씩 빼서 담음
    for j in range(i, m-i):
        ans[i][j] = table.popleft() # 위
    for j in range(i+1, n-i-1):
        ans[j][m-i-1] = table.popleft() # 오른쪽
    for j in range(m-i-1,i-1,-1):
        ans[n-i-1][j] = table.popleft() # 아래
    for j in range(n-i-2, i, -1):
        ans[j][i] = table.popleft() # 왼쪽

for line in ans:
    print(*line)
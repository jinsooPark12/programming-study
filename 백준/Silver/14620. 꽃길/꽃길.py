import sys
input = sys.stdin.readline

def check(x, y, visited):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx, ny) in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer:
        return
    if len(visited) == 15:
        answer = total
    else:
        for i in range(1, N-1):
            for j in range(1, N-1):
                if check(i, j, visited) and (i,j) not in visited:
                    temp = [(i,j)]
                    temp_cost = matrix[i][j]
                    for k in range(4):
                        ni = i + dx[k]
                        nj = j + dy[k]
                        temp.append((ni, nj))
                        temp_cost += matrix[ni][nj]
                    dfs(visited + temp, total + temp_cost)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = int(input())
answer = 1000000

matrix = [list(map(int, input().split())) for _ in range(N)]
dfs([],0)

print(answer)
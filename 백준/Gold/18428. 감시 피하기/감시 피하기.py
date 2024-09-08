import sys
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# T의 위시에서 상하좌우 일직선 탐색
def check(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # T의 일직선 탐색
        while 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] != 'O':
            if matrix[nx][ny] == 'S':
                # 감시 가능
                return True
            else:
                # T나 X면 계속 탐색
                nx += dx[i]
                ny += dy[i]
    # 감시 불가능
    return False
    
# 벽을 설치할 수 있는 모든 경우 탐색
def find(count, size):
    global ans
    # 벽 3개를 설치했을 때
    if count == 3:
        cnt = 0
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == 'T':
                    if not check(i,j):
                        cnt += 1
        # 모든 선생이 감시 불가능
        if cnt == teacher:
            ans = True
        return
    
    # 재귀를 사용해서 벽 3개 설치
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 'X':
                matrix[i][j] = 'O'
                count += 1
                find(count, size)
                matrix[i][j] = 'X'
                count -= 1
    

N = int(input())
matrix = []
teacher = 0

for _ in range(N):
    data = list(input().strip().split(' '))
    teacher += data.count('T')
    matrix.append(data)

ans = False
find(0,N)
if ans:
    print("YES")
else:
    print("NO")
def dfs(x, y, num):
    # 중복되지 않는 6자리 숫자 확인
    if len(num) == 6:
        if num not in result:
            result.append(num)
        return
    
    # 상하좌우 확인 범위
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        
        if 0 <= ddx < 5 and 0 <= ddy < 5:
            # 6자리 숫자가 될 때까지 재귀
            dfs(ddx, ddy, num + matrix[ddx][ddy])

matrix = [list(map(str, input().split())) for _ in range(5)]
result = []

# 0,0부터 4,4까지 모두 검사, 시작 지점
for i in range(5):
    for j in range(5):
        dfs(i, j, matrix[i][j])

print(len(result))
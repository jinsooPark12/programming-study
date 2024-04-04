from collections import deque  # deque를 사용하기 위해 collections 모듈의 deque import
def solution(land):
    answer = 0
    n = len(land)              # n = land의 요소의 개수(세로 길이)
    m = len(land[0])           # m = land[0]의 요소의 개수(가로 길이)
    dx = [0,0,1,-1]            # dx, dy =  선택된 위치에서 주위의 석유를
    dy = [1,-1,0,0]            #           탐색할 수 있게 이동할 위치
    result = [0 for i in range(m+1)]                           # 계산된 결과를 저장할 리스트
    visited = [[0 for i in range(m)] for j in range(n)]        # 이미 확인한 위치를 저장하는 리스트
    def bfs(a, b):                               # 석유를 탐색할 수 있는 알고리즘(너비 우선 탐색)
        count = 0                                
        visited[a][b] = 1
        q = deque()
        q.append((a,b))                          # deque q에 a,b를 저장
        min_y, max_y = b, b                      # 계산의 결과값을 result에 저장하기 위한 범위
        while q:                                 # 석유 덩어리를 확인하고 계산하는 반복문, q에 요소가 있다면 참
            x,y = q.popleft()                    # q의 요소가 x와 y에 선입선출
            min_y = min(min_y, y)                # 반복문을 돌면서 y를 계속 갱신하고 이를 통해 min_y와 max_y를 갱신
            max_y = max(max_y, y)
            count += 1
            for i in range(4):                   # x, y의 주위에 석유를 탐색할 수 있도록 하는 반복문
                nx = x + dx[i]                   # dx[i], dy[i]를 x, y에 더함으로 위치 좌표 변경
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:          # 변경된 값이 land 리스트의 범위에서 나갈 경우 건너 뜀
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:      # 변경된 위치에 석유가 있고 아직 확인한 곳이 아니라면
                    visited[nx][ny] = 1                             # visited[nx][ny] 값 변경하고 q에 nx,ny를 저장
                    q.append((nx,ny))
        
        for i in range(min_y, max_y+1):                 # 석유 덩어리 계산이 끝나면 result[min_y] ~ result[max_y]에 count 값을 저장
            result[i] += count
    
    for i in range(n):                                          # land의 모든 범위를 순회하며 새로운 석유를 발견하면
        for j in range(m):                                      # bfs 알고리즘으로 이동하여 석유 덩어리 탐색
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    answer = max(result)                      # 모든 탐색이 끝나면 result의 요소 중 값이 가장 큰 요소를 answer에 저장
    return answer
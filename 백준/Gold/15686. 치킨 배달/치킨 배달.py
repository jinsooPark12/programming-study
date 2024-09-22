import sys
input = sys.stdin.readline

home = []
chicken = []
min_ans = 100000000

def dfs(idx, count):
    global min_ans
    
    if count == M:
        ans = 0
        
        for i in home:
            distance = 9999999
            for j in range(len(visited)):
                if visited[j]:
                    check_num = abs(i[0] - chicken[j][0]) + abs(i[1] - chicken[j][1])
                    distance = min(distance, check_num)
            ans += distance
        min_ans = min(min_ans, ans)
        return
    
    for i in range(idx, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,count+1)
            visited[i] = False

N, M = map(int, input().split())
for i in range(N):
    matrix = list(map(int,input().split()))
    for j in range(N):
        if matrix[j] == 1:
            home.append((i,j))
        elif matrix[j] == 2:
            chicken.append((i,j))

visited = [False] * len(chicken)

dfs(0,0)
print(min_ans)
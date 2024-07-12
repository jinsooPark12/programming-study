from collections import deque
import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(len(graph)):
    graph[i] = sorted(graph[i])

visited = [False] * (N+1)
dfs(graph, V, visited)

print()

visited = [False] * (N+1)
bfs(graph, V, visited)
# 모든 노드의 경우의 수를 볼 수 있게 dfs와 백트레킹을 사용

def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for current, next in edges:
            if visited[current] and not visited[next]:
                visited[next] = 1
                # 다음 노드가 양일때
                if info[next] == 0:
                    dfs(sheep+1, wolf)
                # 다음 노드가 늑대일때
                else:
                    dfs(sheep, wolf+1)
                # 백트레킹
                visited[next] = 0
    visited[0] = 1
    dfs(1, 0)
    return max(answer)
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
                if info[next] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[next] = 0
    visited[0] = 1
    dfs(1, 0)
    return max(answer)
import heapq

def solution(n, paths, gates, summits):
    answer = [0, 10000001]
    summits = set(summits)
    gates = set(gates)
    intensity = [10000001] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append([j,w])
        graph[j].append([i,w])

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0,start))
        intensity[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if now in summits:
                continue
            if intensity[now] < dist:
                continue
            for i in graph[now]:
                if i[0] in gates:
                    continue
                cost = max(intensity[now], i[1])
                if cost < intensity[i[0]]:
                    intensity[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
    for start in gates:
        dijkstra(start)
    
    for target in summits:
        if intensity[target] < answer[1]:
            answer = [target, intensity[target]]
        elif intensity[target] == answer[1]:
            answer[0] = min(target, answer[0])
    
    return answer
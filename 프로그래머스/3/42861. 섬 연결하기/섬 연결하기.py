def solution(n, costs):
    answer = 0
    parent = [i for i in range(n+1)]

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    costs.sort(key = lambda x : x[2])

    for i in range(len(costs)):
        a, b, cost = costs[i]
        if find(parent,a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer
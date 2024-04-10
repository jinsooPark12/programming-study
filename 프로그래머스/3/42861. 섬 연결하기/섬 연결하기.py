# 가장 적은 비용으로 모든 노드를 연결
# -> 최소 신장 트리
# -> 크루스칼 알고리즘
def solution(n, costs):
    answer = 0
    # 부모 테이블
    # 부모와 값이 같은 원소로 초기화하여 자기 자신을 부모로
    parent = [i for i in range(n+1)]

    # 부모 노드를 찾는 find 연산
    def find(parent, x):
        if parent[x] != x:                        # 부모 노드와 자식노드가 같이 않다면
            parent[x] = find(parent, parent[x])   # 부모 노드를 자식으로 하는 부모노드 탐색
        return parent[x]                          # 부모 노드와 자식 노드가 같다면 부모 노드 반환
    
    # 부모-자식 관계 형성 -> union 연산
    def union(parent, a, b):
        # a와 b의 각 부모 노드 탐색
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 주어진 비용을 기준으로 오름차순 정렬
    costs.sort(key = lambda x : x[2])

    for i in range(len(costs)):
        a, b, cost = costs[i]
        # find 연산 후, a와 b의 부모 노드가 다르면 union 연산 수행 => 최소 신장 트리 추가
        if find(parent,a) != find(parent, b):
            union(parent, a, b)
            answer += cost

    return answer
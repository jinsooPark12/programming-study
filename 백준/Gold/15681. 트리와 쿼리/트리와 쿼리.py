import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def makeTree(currentNode, parent, tree):
    for Node in connect[currentNode]:
        if Node != parent:
            tree[currentNode].append(Node)
            makeTree(Node, currentNode, tree)

def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for Node in tree[currentNode]:
        countSubtreeNodes(Node)
        size[currentNode] += size[Node]

N, R, Q = map(int, input().split())

connect = [[] for _ in range(N+1)]
tree = [[] for _ in range(N+1)]
size = [0 for _ in range(N+1)]

for i in range(N-1):
    start, end = map(int, input().split())
    connect[start].append(end)
    connect[end].append(start)

makeTree(R, -1, tree)
countSubtreeNodes(R)

for _ in range(Q):
    print(size[int(input())])
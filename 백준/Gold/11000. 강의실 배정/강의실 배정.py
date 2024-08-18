# 처음엔 받은 입력값(종료 시간)을 배열에 넣고 나중에 입력되는 입력값(시작 시간)과 비교하는
# 이중 for문을 사용 => 시간 초과

# 이중 for문이 필요했던 이유인 최소 시간을 찾는 것을 위해 우선순위 큐를 사용

import sys
import heapq
input = sys.stdin.readline

n = int(input())

time = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x: (x[0], x[1]))

heap = [time[0][1]]
for i in range(1, n):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, time[i][1])

print(len(heap))
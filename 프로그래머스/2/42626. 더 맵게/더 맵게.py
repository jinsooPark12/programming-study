import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while 1:
        num1 = heapq.heappop(scoville)
        if num1 >= K:
            return answer
        if len(scoville) == 0:
            return -1
        else:
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1+(num2*2))
            answer += 1
    return answer
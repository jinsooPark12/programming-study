import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        num1 = heapq.heappop(scoville)
        if num1 >= K:
            return answer
        else:
            num2 = heapq.heappop(scoville)
            heapq.heappush(scoville, num1+(num2*2))
            answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer
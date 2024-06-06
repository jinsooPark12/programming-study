# 두 큐의 원소의 합을 같게 -> queue1의 원소의 합 = (모든 원소의 합 // 2) 이면 성립

from collections import deque

def solution(queue1, queue2):
    answer = 0
    # sum(큐)를 반복문에 넣으면 시간초과
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    total = sum_queue1 + sum_queue2
    if total % 2 == 0:
        total = total // 2
    else: 
        return -1
    # 두 큐의 최대 교환 횟수
    n2 = len(queue1)*3
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while 1:
        if sum_queue1 == total:
            return answer
        if answer >= n2:
            return -1
        # queue1의 합 > (모든 원소의 합 // 2)
        if sum_queue1 > total:
            num = queue1.popleft()
            queue2.append(num)
            sum_queue1 -= num
            answer += 1
        # queue1의 합 < (모든 원소의 합 // 2)
        if sum_queue1 < total:
            num = queue2.popleft()
            queue1.append(num)
            sum_queue1 += num
            answer += 1
    return answer
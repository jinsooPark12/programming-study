from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)
    total = sum_queue1 + sum_queue2
    if total % 2 == 0:
        total = total // 2
    else: 
        return -1
    n2 = len(queue1)*4
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while 1:
        if sum_queue1 == total:
            return answer
        if answer >= n2:
            return -1
        if sum_queue1 > total:
            num = queue1.popleft()
            queue2.append(num)
            sum_queue1 -= num
            answer += 1
        if sum_queue1 < total:
            num = queue2.popleft()
            queue1.append(num)
            sum_queue1 += num
            answer += 1
    return answer
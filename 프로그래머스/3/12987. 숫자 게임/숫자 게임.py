def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    if min(A) > max(B):
        return 0
    while len(A) != 0:
        num1 = A.pop(0)
        for i in range(len(B)):
            num2 = B.pop(0)
            if num2 > num1:
                answer += 1
                break
    return answer
# 단순히 반복문만을 사용한 구현 -> 당연히 효율성 0
# 효율성 통과를 위해 이분 탐색 사용

def solution(stones, k):
    answer = 0
    # 탐색의 범위 설정(한 디딤돌을 건널 수 있는 최대, 최소 사람 수)
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        check = 0
        # mid 명의 사람들이 디딤돌을 건널 때 한번에 건너 뛰어야 하는 디딤돌의 수 계산
        for stone in stones:
            if (stone - mid) <= 0:
                check += 1
            else:
                check = 0
            if check >= k:
                break
        if check < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1
    return answer
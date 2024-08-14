# LIS 이분탐색 문제

def binary_search(target, lis):
    start = 0
    end = len(lis) - 1
    while start < end:
        mid = (start+end) // 2
        
        # 중간값이 타겟과 같다면 중간값의 위치를 반환
        if lis[mid] == target:
            return mid
        
        # 타겟보다 큰 값 중 가장 작은 값의 위치는
        # 아래와 같이 바로 전 값보다 크면서 바로 현재 값보단 작은 위치임
        elif lis[mid-1] < target < lis[mid]:
            return mid
        
        # target이 더 작으면 왼쪽 탐색
        elif target < lis[mid]:
            end = mid - 1
            
        # target이 더 크면 오른쪽 더 탐색
        else:
            start = mid + 1
    return start    # 만약 시작점과 끝점이 같다면 시작점을 반환

n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for i in range(1,n):
    target = A[i]
    if target > dp[-1]:
        dp.append(target)
    else:
        index = binary_search(target, dp)
        dp[index] = target
        
print(len(dp))
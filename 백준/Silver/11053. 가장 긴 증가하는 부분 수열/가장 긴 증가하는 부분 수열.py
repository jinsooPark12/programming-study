# 증가하는 부분 수열
# 전형적인 dp문제

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N    # arr[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

for i in range(1,N):
    for j in range(i):
        # 선택한 요소(i)와 그 이전에 있는 요소들(j)의 크기 비교
        if arr[i] > arr[j]:
            # 선택한 값이 크면 dp[i]와 그 이전 값들을 비교 후 값 변경
            # 즉 arr[i]보다 작은 위치에 있는 것들 중 dp 테이블 값이 제일 큰 값으로 바꿔주면 됨
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))
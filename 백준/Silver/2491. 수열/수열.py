import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[1]*N for _ in range(2)]

for i in range(1,N):
    if arr[i-1] <= arr[i]:
        dp[0][i] = dp[0][i-1]+1
    if arr[i-1] >= arr[i]:
        dp[1][i] = dp[1][i-1]+1

print(max(map(max,dp)))
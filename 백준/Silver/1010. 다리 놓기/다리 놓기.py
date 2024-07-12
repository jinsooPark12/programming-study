import sys
input = sys.stdin.readline

arr = [[0] * 30 for _ in range(30)]

for i in range(30):     # 배열 초기화
    arr[i][1] = i       # i개 중 1개를 뽑는 경우의 수
    arr[i][0] = 1       # i개 중 0개를 뽑는 경우의 수
    arr[i][i] = 1       # i개 중 i개를 뽑는 경우의 수

# 조합의 점화식
for i in range(2, 30):
    for j in range(1,i):
        # i개 중 j개를 뽑는 경우의 수 = (i-1개 중 j개를 뽑는 경우의 수) + (i-1개 중 j-1개를 뽑는 경우의 수)
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    result = arr[M][N]
    print(result)
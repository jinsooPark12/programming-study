n = int(input())
a = list(map(int,input().split()))

dp = [1] * n    # a[i]를 마지막 값으로 가지는 가장 긴 증가부분수열의 길이

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]:
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰 값을 대입
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))

answer = []         # 정답수열을 입력할 배열선언
order = max(dp)     # 가장 큰 값부터 찾기 위해 max(dp) 저장
for i in range(n - 1, -1, -1):
    if dp[i] == order:
        answer.append(a[i])
        order -= 1
        
answer.reverse()    # 큰 수부터 작은 수로 뽑았기 때문에
print(*answer)
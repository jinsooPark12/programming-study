dp = [0]*1001
dp[0] = 1
dp[1] = 3

for i in range(2,len(dp)):
    dp[i] = (dp[i-1] + (dp[i-2]*2)) % 10007
    
n = int(input())
print(dp[n-1])
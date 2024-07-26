dp = [0]*251
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, len(dp)):
    dp[i] = dp[i-1] + (dp[i-2]*2)
    
while 1:
    try: n = int(input())
    except: break
    
    print(dp[n])
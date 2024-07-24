# dp
# 방법1: 현재 자리숫자가 0보다 클 때 -> 이전 dp값을 더함
# => 이전 dp가 가지는 방법들 뒤에 한 자리수로 추가하기만 하면 되므로
# ex) 25114에서 2511까지 구했다고 하면 2 5 1 1 / 25 1 1 / 2 5 11 / 25 11

# 방법2: 이전 자리수와 현재 자리수를 두 자리숫자로 볼 때 10~26사이의 숫자에 해당할 때
# => 전 전 dp 값을 더함

n = list(map(int, input()))

dp = [0 for _ in range(len(n)+1)]

if (n[0] == 0):
    print("0")
else:
    n = [0] + n
    dp[0] = dp[1] = 1
    for i in range(2, len(n)):
        if n[i] > 0:
            dp[i] += dp[i-1]
        temp = n[i-1] * 10 + n[i]
        if temp >= 10 and temp <= 26:
            dp[i] += dp[i-2]
    print(dp[len(n)-1] % 1000000)
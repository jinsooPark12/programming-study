import math
k = int(input())
n = 10

ans = math.factorial(n+k-1)//((math.factorial(n-1))*(math.factorial(k)))

print(ans%10007)
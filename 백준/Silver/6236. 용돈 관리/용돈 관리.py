n, m = map(int, input().split())
money = list(int(input()) for _ in range(n))
left, right = min(money),sum(money)

while left <= right:
    mid = (left + right) // 2
    temp = mid
    cnt = 1
    for i in range(n):
        if temp < money[i]:
            temp = mid
            cnt += 1
        temp -= money[i]
    
    if mid < max(money) or cnt > m:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
        
print(ans)
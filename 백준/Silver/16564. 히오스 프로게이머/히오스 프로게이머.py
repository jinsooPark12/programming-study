n, k = map(int, input().split())
X = sorted([int(input()) for _ in range(n)])

left= min(X)
right = left + k

ans = 0
while left <= right:
    total = 0
    mid = (left + right) // 2
    for x in X:
        if mid > x:
            total += mid - x
    if total <= k:
        left = mid + 1
        ans = max(mid, ans)
    else:
        right = mid - 1
        
print(ans)
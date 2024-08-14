def binary_search(target, lis):
    start = 0
    end = len(lis) - 1
    while start < end:
        mid = (start+end) // 2
        
        if lis[mid] == target:
            return mid
        elif lis[mid-1] < target < lis[mid]:
            return mid
        elif target < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return start

n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for i in range(1,n):
    target = A[i]
    if target > dp[-1]:
        dp.append(target)
    else:
        index = binary_search(target, dp)
        dp[index] = target
        
print(len(dp))
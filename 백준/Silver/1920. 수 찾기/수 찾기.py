import sys
input = sys.stdin.readline

def findNumber(num):
    start = 0
    end = n-1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0
            
n = int(input())
# arr = list(map(int, input().split())).sort()
# 이거 왜 None이지?
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    ans = findNumber(num)
    print(ans)
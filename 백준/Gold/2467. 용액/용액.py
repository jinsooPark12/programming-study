# 이분 탐색

IFT = 100000000000000000000
x, y = 0, 0
N = int(input())

arr = list(map(int, input().split()))
left, right = 0, N-1

while (left < right):
    checkNum = arr[left] + arr[right]
    
    if abs(checkNum) <= IFT:
        IFT = abs(checkNum)
        x = arr[left]
        y = arr[right]
        
    if checkNum <= 0:
        left += 1

    else:
        right -= 1

print(x,y)
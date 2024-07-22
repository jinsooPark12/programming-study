import sys
input = sys.stdin.readline

arr = [0 for _ in range(11)]
arr[0], arr[1], arr[2] = 1,2,4
    
for i in range(3,len(arr)):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

for _ in range(int(input())):
    n = int(input())
    print(arr[n-1])
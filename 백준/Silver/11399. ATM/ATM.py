N = int(input())
arr = list(map(int, input().split()))

minSum = 0
total = 0
arr.sort()

for i in arr:
    minSum += i
    total += minSum

print(total)
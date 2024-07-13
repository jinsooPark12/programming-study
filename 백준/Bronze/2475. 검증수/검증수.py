total = 0
arr = list(map(int, input().split()))
for i in range(5):
    total += pow(arr[i],2)
print(total % 10)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

result = end = 0

for s, e in arr:
   if s >= end:
       end = e
       result += 1

print(result)
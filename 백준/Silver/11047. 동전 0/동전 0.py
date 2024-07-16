N, K = map(int, input().split())

money = sorted([int(input()) for _ in range(N)],reverse=True)
result = 0

i = 0
while K != 0:
    if money[i] > K:
        i += 1
    else:
        result += K // money[i]
        K = K % money[i]

print(result)
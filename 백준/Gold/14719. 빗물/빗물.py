H,W = map(int, input().split())

matrix = [[0]*W for _ in range(H)]

block = list(map(int, input().split()))
temp = [H - block[i] for i in range(W)]

for i in range(H):
    for j in range(W):
        if i < temp[j]:
            continue
        matrix[i][j] = 1

ans = 0
for i in range(H):
    sum = 0
    flag = 0
    for j in range(W):
        if matrix[i][j] == 0:
            if not flag:
                continue
            sum += 1
        else:
            if not flag:
                flag = 1
                continue
            ans += sum
            sum = 0
            
print(ans)
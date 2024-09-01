from sys import stdin
input = stdin.readline

prime = []              # 소수 배열
check = [1] * 1000001  # 인덱스가 소수 = 1, 아니면 = 0
# 0과 1은 소수가 아님
check[0] = check[1] = 0

for i in range(2,1000001):
    if check[i] == 1:
        prime.append(i)
        for j in range(2*i,1000001,i):
            check[j] = 0

T = int(input())

for _ in range(T):
    ans = 0
    N = int(input())
    for i in prime:
        if i >= N:
            break
        if check[N-i] and i <= N-i:
            ans += 1
    print(ans)
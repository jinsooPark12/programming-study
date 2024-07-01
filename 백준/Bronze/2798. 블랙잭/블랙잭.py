import sys

N,M = map(int, sys.stdin.readline().split())
card = sorted(map(int, sys.stdin.readline().split()), reverse=True)
result = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            myCard = card[i]+card[j]+card[k]
            if myCard <= M:
                if result < myCard:
                    result = myCard
print(result)
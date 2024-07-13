arr=[list(map(int,input().split())) for _ in range(int(input()))]
deadline=10000000
arr.sort(key = lambda x : -x[1])
for t,s in arr:
    deadline = min(s,deadline)
    deadline -= t
    
if deadline < 0:
    print(-1)
else:
    print(deadline)
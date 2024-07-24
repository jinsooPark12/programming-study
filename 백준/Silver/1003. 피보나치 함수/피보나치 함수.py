import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    a,b = 1,0               # 0과 1이 호출된 횟수
    for i in range(n):
        a, b = b, a+b       # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼
    print(a,b)
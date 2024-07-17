import sys

def decimal(n):
    aray = [True] * n
    m = int(n**0.5)
    for i in range(2, m+1):
        if aray[i] == True:
            for j in range(i+i, n, i):
                aray[j] = False
    return [i for i in range(2,n) if aray[i] == True]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dc = decimal(n)
    n2 = n//2

    for i in range(5001):
        if n2-i in dc and n2+i in dc:
            print(f"{n2-i} {n2+i}")
            break
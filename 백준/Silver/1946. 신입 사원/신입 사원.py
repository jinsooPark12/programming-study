import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    grade = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
    
    max_grade = grade[0][1]
    result = 1
    for i in range(1,n):
        cur_grade = grade[i][1]
        if cur_grade > max_grade:
            continue
        max_grade = cur_grade
        result += 1
    
    print(result)
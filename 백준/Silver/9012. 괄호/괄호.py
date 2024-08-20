import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    flag = 1
    right = left = 0 
    ps = input().rstrip()
    if ps[0] != "(" or ps[-1] != ")":
         print("NO")
         continue
    for p in ps:
        if right < left:
            print("NO")
            flag = 0
            break
        if p == "(":
            right += 1
        elif p == ")":
            left += 1
        else:
            continue
    if right == left and flag == 1:
        print("YES")
    elif right != left and flag == 1: 
        print("NO")
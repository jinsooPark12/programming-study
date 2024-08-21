while 1:
    S = input()
    flag = 1
    stack = []
    count = -1
    
    if S == ".":
        break
    
    for s in S:
        if s == "(":
            stack.append(1)
        elif s == "[":
            stack.append(2)
        elif s == ")":
            if len(stack) == 0:
                flag = 0
                break
            if stack[-1] != 1:
                flag = 0
                break
            else: 
                stack.pop()
        elif s == "]":
            if len(stack) == 0:
                flag = 0
                break
            if stack[-1] != 2:
                flag = 0
                break
            else: stack.pop()
        else:
            continue
    
    if len(stack) != 0:
        flag = 0
    if flag:
        print("yes")
    else:
        print("no")
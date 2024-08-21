S = input()
stack = []
count = 0
result = ""
flag = 1

for s in S:
    if s == "<":
        flag = 0
        if count != 0:
            for _ in range(count):
                result += stack.pop()
            count = 0
        result += s
    elif s == ">":
        flag = 1
        result += s
    elif s == " " and flag:
        for _ in range(count):
            result += stack.pop()
        result += " "    
        count = 0
    else:
        if flag:
            stack.append(s)
            count += 1
        else:
            result += s

if len(stack) != 0:
    for _ in range(count):
        result += stack.pop()
print(result)
def solution(before, after):
    a = 0
    b = 0
    for i in range(len(before)):
        b += int(ord(before[i]))
    for j in range(len(after)):
        a += int(ord(after[j]))
    if a == b:
        answer = 1
    else:
        answer = 0
    return answer
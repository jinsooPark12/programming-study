str = input()
stack = []
length = len(str)
result = 0
count = 0

for i in range(length):
    if str[i] == "(":
        count += 1
    else:
        if str[i-1] == "(":
            count -= 1
            result += count
        else:
            count -= 1
            result += 1

print(result)
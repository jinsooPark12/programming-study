n = int(input())
max_x, min_x = -99999, 99999
max_y, min_y = -99999, 99999
for i in range(n):
    x,y = map(int, input().split())
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y
total_x = max_x - min_x
total_y = max_y - min_y
answer = total_x * total_y
print(answer)
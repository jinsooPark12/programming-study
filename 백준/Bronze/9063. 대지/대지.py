import sys
max_x = max_y = -9999999
min_x = min_y = 9999999

for _ in range(int(sys.stdin.readline())):
    x,y = map(int, sys.stdin.readline().split())
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y

print((max_x - min_x)*(max_y - min_y))
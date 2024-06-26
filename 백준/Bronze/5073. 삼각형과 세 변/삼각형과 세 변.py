import sys

while 1:
    x, y, z = map(int, sys.stdin.readline().split())

    if x == y == z == 0:
        break
    if max(x,y,z) >= ((x + y + z) - max(x,y,z)):
        print("Invalid")
    else:
        if x == y == z:
            print("Equilateral")
        elif x == y or y == z or z == x:
            print("Isosceles")
        else:
            print("Scalene")
import sys
arr = [0,0,0]
total = 0
for i in range(3):
    arr[i] = int(sys.stdin.readline())
    total += arr[i]

if total != 180:
    print("Error")
else:
    if arr[0] == arr[1] == arr[2]:
        print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0]:
        print("Isosceles")
    else:
        print("Scalene")
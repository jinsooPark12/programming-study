import sys
n = [i for i in range(666,5000000) if "666" in str(i)]
print(n[int(sys.stdin.readline())-1])
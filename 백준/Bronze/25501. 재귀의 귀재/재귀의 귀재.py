def recursion(s, l, r, num):
    if l >= r: return 1, num
    elif s[l] != s[r]: return 0, num
    else: return recursion(s, l+1, r-1, num+1)

def isPalindrome(s, num):
    return recursion(s, 0, len(s)-1, num)

for _ in range(int(input())):
    s = input()
    ans1, ans2 = isPalindrome(s, 1)
    print(ans1, ans2)
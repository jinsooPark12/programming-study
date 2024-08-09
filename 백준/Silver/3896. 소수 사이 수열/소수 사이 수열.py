import math

n = 1299709 # 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
T = int(input())
for _ in range(T):
    ans = 0
    k = int(input())
    if array[k]:
        print(ans)
    else:
        ans += 1
        right = k+1
        left = k-1
        while not (array[left] and array[right]):
            if not array[left]:
                ans += 1
                left -= 1
            if not array[right]:
                ans += 1
                right += 1
        print(ans+1)
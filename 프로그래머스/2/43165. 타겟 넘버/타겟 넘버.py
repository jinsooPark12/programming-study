# 계산되는 합의 결과를 모두 탐색
# 음수와 양수의 경우를 모두 따져봐야하기 때문에 dfs 알고리즘 사용
def dfs(ans, n, numbers, target):
        global answer
        if n == len(numbers):
            if ans == target:
                answer += 1
            return
        dfs(ans + numbers[n], n + 1, numbers, target)
        dfs(ans - numbers[n], n + 1, numbers, target)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0,0, numbers, target)
    return answer
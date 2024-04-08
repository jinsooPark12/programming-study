def solution(numbers, target):
    global answer
    answer = 0
    def dfs(number, n):
        global answer
        if n == len(numbers):
            if number == target:
                answer += 1
                return
            return
        dfs(number + numbers[n], n + 1)
        dfs(number - numbers[n], n + 1)
    dfs(0, 0)
    return answer
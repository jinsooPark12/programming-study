def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(n-i):
            a = j
            b = j + i
            for k in range(a,b):
                if dp[a][b] != 0:
                    dp[a][b] = min(dp[a][b], dp[a][k] + dp[k+1][b] + (matrix_sizes[a][0] * matrix_sizes[k][1] * matrix_sizes[b][1]))
                else:
                    dp[a][b] = dp[a][k] + dp[k+1][b] + (matrix_sizes[a][0] * matrix_sizes[k][1] * matrix_sizes[b][1])
    return dp[0][n-1]
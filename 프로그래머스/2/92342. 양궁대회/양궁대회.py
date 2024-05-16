from itertools import product
def solution(n, info):
    info.reverse()
    ans = [-1]
    maxScore = 0
    for TF in product((True, False), repeat = 11):          # 각각의 점수에서 이긴 경우와 진 경우를 전부 계산
        s = sum(info[i]+1 for i in range(11) if TF[i])      # 각 경우의 화살 개수 계산
        if s <= n:
            # apeach와 ryan 점수 계산
            apeach = sum(i for i in range(11) if not TF[i] and info[i])
            ryan = sum(i for i in range(11) if TF[i])
            score = ryan - apeach
            if score > maxScore:
                maxScore = score
                ans = [info[i]+1 if TF[i] else 0 for i in range(11)]
                ans[0] += n-s
    ans.reverse()
    return ans
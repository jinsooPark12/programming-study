def solution(targets):
    answer = 0
    T = 0                       # 요격의 제한범위
    for s, e in sorted(targets):
        # s가 제한범위 내에 있다면
        if T > s:
            T = min(T, e)
        # s가 제한범위 밖에 있다면
        else:
            answer += 1
            T = e-0.5           # 요격한 미사일의 끝 범위인 e로 제한범위 변경, 실수를 고려해서 0.5를 뺌
    return answer
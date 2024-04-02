def solution(targets):
    answer = 0
    T = 0                # 요격의 제한범위
    for s, e in sorted(targets):
        # s가 제한범위 내에 있다면
        if T > s:
            T = min(T,e)
        # s가 제한범위 밖에 있다면
        else:
            answer += 1
            T = e-0.5
    return answer
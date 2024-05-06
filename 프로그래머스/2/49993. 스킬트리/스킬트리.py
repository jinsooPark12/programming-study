def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        user_skill = ""
        for j in i:
            if j in skill:
                user_skill += j
        if user_skill == skill[:len(user_skill)]:
            answer += 1

    return answer
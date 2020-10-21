def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        idx = 0
        breaker = False
        for s in st:
            i = skill.find(s, idx)
            if i == -1: continue
            if idx != i:
                breaker = True
            idx += 1
        if not breaker:
            answer += 1
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	)
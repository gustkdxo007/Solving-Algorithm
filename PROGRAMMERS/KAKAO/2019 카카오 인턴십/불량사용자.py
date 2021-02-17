# def solution(user_id, banned_id):
#     answer = 0
#     candidate = [[] for _ in range(len(banned_id))]
#     for b in range(len(banned_id)):
#         for user in user_id:
#             if len(banned_id[b]) != len(user): continue
#             check = True
#             for i in range(len(user)):
#                 if banned_id[b][i] == '*': continue
#                 if banned_id[b][i] != user[i]:
#                     check = False
#                     break
#             if check:
#                 candidate[b].append(user)
#     candidate = list(map(tuple, candidate))
#     print(list(set(candidate)))
#     return answer

from itertools import permutations

def solution(user_id,banned_id):
    answer = []
    candidate = permutations(user_id, len(banned_id))
    for cand in candidate:
        check = True
        for i in range(len(banned_id)):
            if len(banned_id[i]) != len(cand[i]):
                check = False
                break
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == '*': continue
                if banned_id[i][j] != cand[i][j]:
                    check = False
                    break
            if not check: break
        if check:
            cand = set(cand)
            if cand not in answer:
                answer.append(cand)
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))


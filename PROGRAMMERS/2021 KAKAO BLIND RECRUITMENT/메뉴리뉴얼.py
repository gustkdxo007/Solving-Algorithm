from itertools import combinations

def solution(orders, course):
    answer = []
    for cnt in course:
        candidates = dict()
        max_cnt = 0
        for order in orders:
            for comb in combinations(order, cnt):
                menu = ''.join(sorted(comb))
                if menu in candidates:
                    candidates[menu] += 1
                    max_cnt = max(max_cnt, candidates[menu])
                else:
                    candidates[menu] = 1
        if max_cnt < 2: continue
        for comb_menu, num in candidates.items():
            if num == max_cnt:
                answer.append(comb_menu)
    answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
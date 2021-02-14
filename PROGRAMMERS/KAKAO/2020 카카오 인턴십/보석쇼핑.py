import heapq
def solution(gems):
    N = len(set(gems))
    candidates = []
    a = b = 0
    gems_dict = dict()
    while b <= len(gems):
        cnt = len(gems_dict)
        if cnt == N:
            if not len(candidates) or b-a < candidates[0][0]:
                heapq.heappush(candidates, (b-a, [a+1, b]))
            gems_dict[gems[a]] -= 1
            if gems_dict[gems[a]] == 0:
                del gems_dict[gems[a]]
            a += 1
        else:
            if b >= len(gems): break
            if gems[b] in gems_dict:
                gems_dict[gems[b]] += 1
            else:
                gems_dict[gems[b]] = 1
            b += 1
    return heapq.heappop(candidates)[1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))

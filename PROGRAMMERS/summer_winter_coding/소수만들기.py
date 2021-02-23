from itertools import combinations

def solution(nums):
    answer = 0
    sosu = [1] * (50*100 + 1)
    sosu[0], sosu[1] = 0, 0
    for i in range(2, len(sosu)):
        if not sosu[i]: continue
        n = i + i
        while n < len(sosu):
            sosu[n] = 0
            n += i
    for comb in combinations(nums, 3):
        if sosu[sum(comb)]:
            answer += 1
    return answer


print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
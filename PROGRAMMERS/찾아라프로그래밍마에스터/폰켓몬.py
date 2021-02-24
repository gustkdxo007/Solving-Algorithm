def solution(nums):
    cnt = len(set(nums))
    n = len(nums) // 2
    return n if cnt > n else cnt



print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
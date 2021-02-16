def solution(arr, divisor):
    return sorted(list(filter(lambda x: not (x % divisor), arr))) or [-1]


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3,2,6], 10))
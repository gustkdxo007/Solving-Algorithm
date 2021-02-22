def solution(arr):
    max_ = 1
    for a in arr:
        max_ *= a
    for n in range(max(arr), max_+1):
        breaker = False
        for a in arr:
            if n % a:
                breaker = True
                break
        if not breaker:
            return n


print(solution([2,6,8,14]))
print(solution([1,2,3]))
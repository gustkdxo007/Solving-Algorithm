def solution(n):
    result = 0
    l, r = 1, 1
    sum_ = 1
    for i in range(2, n+1):
        sum_ += i
        r = i
        if sum_ == n:
            result += 1
            continue
        if sum_ > n:
            while l <= r:
                sum_ -= l
                l += 1
                if sum_ == n:
                    result += 1
                    break
                if sum_ < n:
                    break
    return result


print(solution(15))
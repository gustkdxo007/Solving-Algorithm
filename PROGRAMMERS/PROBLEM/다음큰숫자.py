def solution(n):
    b_now = bin(n)
    cnt = b_now.count('1')
    next = n+1
    while True:
        if bin(next).count('1') == cnt:
            return next
        next += 1


print(solution(78))
print(solution(15))
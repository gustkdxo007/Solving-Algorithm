def solution(n):
    ans = 0
    # print(bin(n).count('1'))
    while n:
        if n % 2:
            n -= 1
            ans += 1
        n //= 2
    return ans

print(solution(5))
print(solution(6))
print(solution(5000))
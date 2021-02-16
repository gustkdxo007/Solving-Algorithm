def solution(n):
    answer = 0
    prime = [1] * (n+1)
    for i in range(2, n+1):
        if prime[i] == 0: continue
        tmp = i + i
        answer += 1
        while tmp <= n:
            prime[tmp] = 0
            tmp += i
    return answer


print(solution(10))
print(solution(5))
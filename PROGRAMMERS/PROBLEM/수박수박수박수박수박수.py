def solution(n):
    answer = ''
    if n % 2:
        answer += '수박'*(n//2)
        answer += '수'
    else:
        answer += '수박'*(n//2)
    return answer


print(solution(3))
print(solution(4))
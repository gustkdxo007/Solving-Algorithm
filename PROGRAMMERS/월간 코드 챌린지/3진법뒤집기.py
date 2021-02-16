def solution(n):
    answer = 0
    ternary = ""
    while n > 0:
        ternary += str(n % 3)
        n //= 3
    for i in range(len(ternary)):
        answer += int(ternary[i]) * (3**(len(ternary)-1-i))
    return answer


print(solution(45))
print(solution(125))
print(solution(3))
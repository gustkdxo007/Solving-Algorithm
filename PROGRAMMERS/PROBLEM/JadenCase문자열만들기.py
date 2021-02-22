def solution(s):
    answer = ''
    check = True
    for c in s:
        if c == ' ':
            check = True
            answer += c
        else:
            if check:
                answer += c.upper()
                check = False
            else:
                answer += c.lower()
    return answer




print(solution("3people unFollowed me"))
print(solution("for the last week"))
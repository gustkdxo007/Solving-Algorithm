def solution(s):
    middle = len(s) // 2
    if len(s) % 2:
        return s[middle]
    else:
        return s[middle-1:middle+1]


print(solution("abcde"))
print(solution("qwer"))
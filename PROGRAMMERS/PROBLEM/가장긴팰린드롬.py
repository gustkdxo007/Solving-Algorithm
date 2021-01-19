def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s)-i+1):
            tmp = s[j:i+j]
            rev = tmp[::-1]
            if tmp == rev:
                return i


print(solution('abcdcba'))
print(solution('abacde'))

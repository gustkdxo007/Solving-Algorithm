def solution(s):
    s = s.lower()
    return s.count('y') == s.count('p')

print(solution("pPoooyY"))
print(solution("Pyy"))
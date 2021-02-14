def solution(s):
    answer = []
    tmp = []
    num = ''
    for c in s[1:-1]:
        if c == '{' or (c == ',' and not num): continue
        if c == ',' and num:
            tmp.append(int(num))
            num = ''
            continue
        if c == '}':
            if num:
                tmp.append(int(num))
                num = ''
            answer.append(tmp)
            tmp = []
            continue
        num += c
    answer.sort(key=lambda x: len(x))
    result = []
    for li in answer:
        for n in li:
            if n not in result:
                result.append(n)
    return result


# def solution(s):
#
#     s = Counter(re.findall('\d+', s))
#     print(s)
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
#
# import re
# from collections import Counter


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
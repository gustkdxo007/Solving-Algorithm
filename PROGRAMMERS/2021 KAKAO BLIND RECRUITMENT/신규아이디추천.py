def solution(new_id):
    answer = ''
    step_1 = new_id.lower()
    step_2 = ''
    for i in step_1:
        if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90 or 48 <= ord(i) <= 57 or ord(i) in [45, 46, 95]:
            step_2 += i
    step_3 = ''
    tmp = ''
    for i in step_2:
        if i != '.':
            tmp = ''
            step_3 += i
            continue
        if tmp == '.':
            continue
        step_3 += i
        tmp = '.'
    step_4 = step_3.rstrip('.')
    step_4 = step_4.lstrip('.')
    if not step_4:
        step_4 = 'a'
    step_6 = step_4[:15]
    step_6 = step_6.rstrip('.')
    if len(step_6) <= 2:
        step_6 += step_6[-1] * (3-len(step_6))
    answer = step_6
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution(	"=.="))
print(solution(	"123_.def"))
print(solution("abcdefghijklmn.p"))
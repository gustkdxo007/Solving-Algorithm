def check_bracket(bracket):
    stack = []
    for b in bracket:
        if not stack and b == ')':
            return False
        if b == '(':
            stack.append(b)
        elif b == ')' and stack and stack[-1] == '(':
            stack.pop()
    if stack:
        return False
    return True

def balance_bracket(bracket):
    if not bracket:
        return ""
    balance = 0
    u = v = ''
    for i in range(len(bracket)):
        u += bracket[i]
        if bracket[i] == '(':
            balance -= 1
        elif bracket[i] == ')':
            balance += 1
        if not balance:
            v = bracket[i+1:]
            break
    if check_bracket(u):
        return u + balance_bracket(v)
    else:
        tmp = '('
        tmp += balance_bracket(v)
        tmp += ')'
        tmp_u = u[1:len(u)-1]
        for u in tmp_u:
            if u == '(':
                tmp += ')'
            else:
                tmp += '('
        return tmp



def solution(p):
    answer = balance_bracket(p)
    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
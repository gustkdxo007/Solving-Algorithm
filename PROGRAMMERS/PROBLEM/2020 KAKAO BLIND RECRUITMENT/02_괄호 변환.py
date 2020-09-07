def check_bracket(bracket):
    stack = []
    for b in bracket:
        if b == "(":
            stack.append(b)
        elif b == ")" and stack and stack[len(stack)-1] == "(":
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True

def balance_bracket(bracket):
    if not bracket:
        return ""
    left = right = 0
    u = ""
    v = ""
    for b in bracket:
        if b == "(":
            left += 1
        elif b == ")":
            right += 1
        u += b
        if left and right and left == right:
            v = bracket[right+left:]
            break
    if check_bracket(u):
        return u + balance_bracket(v)
    else:
        tmp = "("
        tmp += balance_bracket(v)
        tmp += ")"
        tmp_u = list(u[1:len(u)-1])
        for i in range(len(tmp_u)):
            if tmp_u[i] == "(":
                tmp_u[i] = ")"
            else:
                tmp_u[i] = "("
        tmp += "".join(tmp_u)
        return tmp


def solution(p):
    answer = ''
    if check_bracket(p):
        answer = p
    else:
        answer = balance_bracket(p)
    return answer

# 다른 사람 풀이
# def solution(p):
#     if p=='': return p
#     r=True; c=0
#     for i in range(len(p)):
#         if p[i]=='(': c-=1
#         else: c+=1
#         if c>0: r=False
#         if c==0:
#             if r:
#                 return p[:i+1]+solution(p[i+1:])
#             else:
#                 return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

INPUT = ["(()())()", ")(", "()))((()"]
for i in INPUT:
    print(solution(i))
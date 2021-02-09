def solution(s):
    stack = []
    for c in s:
        if not stack and c == ')':
            return False
        if c == '(':
            stack.append(c)
        if c == ')' and stack[-1] == '(':
            stack.pop()
    if stack:
        return False
    else:
        return True


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
def solution(s):
    stack = []
    for c in s:
        if not stack or stack[-1] != c:
            stack.append(c)
        else:
            stack.pop()
    return 1 if not stack else 0



print(solution('baabaa'))
print(solution('cdcd'))
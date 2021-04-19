def solution(s):
    left_large = right_large = left_medium = right_medium = left_small = right_small = 0
    for c in s:
        if c == "[":
            left_large += 1
        elif c == "]":
            right_large += 1
        elif c == "{":
            left_medium += 1
        elif c == "}":
            right_medium += 1
        elif c == "(":
            left_small += 1
        elif c == ")":
            right_small += 1
    if left_large != right_large or left_medium != right_medium or left_small != right_small: return 0

    answer = 0

    def is_right(s):
        if s[0] in ")}]": return False
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if len(stack) == 0: return False
                if s[i] == ")" and stack[-1] == "(":
                    stack.pop()
                elif s[i] == "}" and stack[-1] == "{":
                    stack.pop()
                elif s[i] == "]" and stack[-1] == "[":
                    stack.pop()
                else: return False
        if len(stack) > 0: return False
        return True



    for i in range(len(s)):
        if is_right(s): answer += 1
        s = s[1:] + s[0]
    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))
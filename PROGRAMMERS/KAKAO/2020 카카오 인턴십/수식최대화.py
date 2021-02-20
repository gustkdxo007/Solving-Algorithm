from itertools import permutations

def calculate(expressions, symbol):
    expressions = expressions[:]
    for s in symbol:
        tmp = []
        for i in range(len(expressions)):
            if expressions[i] == 'xxx': continue
            if expressions[i] == s:
                t = i + 1
                while expressions[t] == 'xxx' and t < len(expressions):
                    t += 1
                if s == '+':
                    tmp[-1] += expressions[t]
                elif s == '-':
                    tmp[-1] -= expressions[t]
                elif s == '*':
                    tmp[-1] *= expressions[t]
                expressions[t] = 'xxx'
            else:
                tmp.append(expressions[i])
        expressions = tmp
    return expressions[0]

def solution(expression):
    result = 0
    expression_arr = []
    num = ''
    symbol = ['+', '-', '*']
    for i in range(len(expression)):
        if expression[i] in symbol:
            expression_arr.append(int(num))
            expression_arr.append(expression[i])
            num = ''
        else:
            num += expression[i]
    expression_arr.append(int(num))
    for i in permutations(symbol, 3):
        result = max(result, abs(calculate(expression_arr, i)))
    return result



print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
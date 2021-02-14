import itertools

def solution(numbers):
    numbers = list(numbers)
    selected_num = []
    for i in range(1, len(numbers)+1):
        selected = map(''.join, itertools.permutations(numbers, i))
        for s in selected:
            s = int(s)
            if s <= 1: continue
            if s in selected_num: continue
            breaker = False
            for j in range(2, s):
                if s % j == 0:
                    breaker = True
                    break
            if breaker: continue
            selected_num.append(s)

    return len(selected_num)

print(solution('17'))
print(solution('011'))
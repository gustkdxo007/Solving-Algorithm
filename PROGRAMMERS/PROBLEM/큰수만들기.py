def solution(number, k):
    answer = ''
    s, e = 0, k+1
    number = list(map(int, list(number)))
    while e <= len(number):
        tmp = -1
        idx = 0
        for i in range(s, e):
            if number[i] > tmp:
                tmp = number[i]
                idx = i
                if tmp == 9: break
        answer += str(tmp)
        s = idx + 1
        e += 1

    return answer

print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
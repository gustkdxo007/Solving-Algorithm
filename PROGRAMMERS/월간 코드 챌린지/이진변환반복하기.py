def solution(s):
    answer = [0, 0]

    def convert(s):
        zero = s.count('0')
        answer[1] += zero
        num = len(s) - zero
        result = ''
        while num:
            result += str(num % 2)
            num //= 2
        return result[::-1]

    while True:
        answer[0] += 1
        s = convert(s)
        if s == '1':
            break

    return answer




print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
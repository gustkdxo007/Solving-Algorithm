def solution(N, number):
    S = [0, {N}]
    answer = -1
    if N == number:
        return 1
    for i in range(2, 9):
        tmp_s = {int(str(N) * i)}
        for i_half in range(1, i//2+1):
            for x in S[i_half]:
                for y in S[i-i_half]:
                    tmp_s.add(x+y)
                    tmp_s.add(x-y)
                    tmp_s.add(y-x)
                    tmp_s.add(x*y)
                    if x != 0:
                        tmp_s.add(y//x)
                    if y != 0:
                        tmp_s.add(x//y)
        print(tmp_s)
        if number in tmp_s:
            return i
        S.append(tmp_s)
    return answer


print(solution(5, 5))
print(solution(2, 11))
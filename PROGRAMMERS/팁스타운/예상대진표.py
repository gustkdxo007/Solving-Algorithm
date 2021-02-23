def solution(N, A, B):
    answer = 0
    A -= 1
    B -= 1
    while N > 0:
        answer += 1
        A //= 2
        B //= 2
        if A == B:
            return answer
        N // 2


print(solution(8, 4, 7))
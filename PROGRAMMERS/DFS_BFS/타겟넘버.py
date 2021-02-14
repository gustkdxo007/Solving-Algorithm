def solution(numbers, target):
    answer = 0
    N = len(numbers)
    def cal(s, t):
        nonlocal answer
        if t == target and s == N:
            answer += 1
            return
        if s == N:
            return

        cal(s+1, t+numbers[s])
        cal(s+1, t-numbers[s])
    cal(0, 0)
    return answer

solution([1,1,1,1,1], 3)
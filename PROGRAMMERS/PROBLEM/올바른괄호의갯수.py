def solution(n):
    answer = 0
    open = close = 0
    def dfs(open, close):
        nonlocal answer
        if open == n and close == n:
            answer += 1
            return
        if close > open or open > n or close > n: return
        dfs(open + 1, close)
        dfs(open, close + 1)
    dfs(open, close)
    return answer


print(solution(2))
print(solution(5))
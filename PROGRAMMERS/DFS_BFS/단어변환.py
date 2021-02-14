def solution(begin, target, words):
    answer = 1e9
    visited = [0]*len(words)
    def dfs(begin, cnt):
        nonlocal answer
        if begin == target:
            answer = min(answer, cnt)
            return
        for i in range(len(words)):
            if visited[i]: continue
            tmp = 0
            for j in range(len(begin)):
                if begin[j] != words[i][j]:
                    tmp += 1
            if tmp == 1:
                visited[i] = 1
                dfs(words[i], cnt+1)
                visited[i] = 0
    dfs(begin, 0)
    return answer if answer != 1e9 else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("hit", "hhh", ["hhh", "hht"]))
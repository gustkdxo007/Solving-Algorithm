def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j]:
                graph[i].append(j)
    visited = [0] * n
    def dfs(n):
        if visited[n]: return
        visited[n] = 1
        for g in graph[n]:
            dfs(g)
    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(i)
    return answer

solution(3, [[1,1,0], [1,1,0], [0,0,1]])
solution(3, [[1,1,0], [1,1,1], [0,1,1]])
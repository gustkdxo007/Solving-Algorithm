from collections import deque

def solution(n, results):
    answer = 0
    victory = [[] for _ in range(n+1)]
    loss = [[] for _ in range(n+1)]
    for a, b in results:
        victory[b].append(a)
        loss[a].append(b)
    for i in range(1, n+1):
        visited = [0] * (n+1)
        Q = deque()
        Q.append(i)
        while Q:
            now = Q.pop()
            if not visited[now]:
                visited[now] = 1
                for j in victory[now]:
                    Q.append(j)
        visited[i] = 0
        Q.append(i)
        while Q:
            now = Q.pop()
            if not visited[now]:
                visited[now] = 1
                for j in loss[now]:
                    Q.append(j)
        if sum(visited[1:]) == n:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
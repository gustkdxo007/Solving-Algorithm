from collections import deque

def solution(n, path, order):
    G = [[] for _ in range(n)]
    for s, t in path:
        G[s].append(t)
        G[t].append(s)
    visited = [0] * n
    check = [0] * n
    before = dict()
    after = dict()
    for s, t in order:
        before[t] = s
        after[s] = t
    Q = deque()
    Q.append(0)
    visited[0] = 1

    while Q:
        node = Q.popleft()
        check[node] = 1
        if not before.get(node):
            visited[node] = 1
            for next in G[node]:
                if visited[next]: continue
                Q.append(next)
            if after.get(node) and check[after[node]]:
                Q.append(after[node])
        else:
            if visited[before[node]]:
                visited[node] = 1
                for next in G[node]:
                    if visited[next]: continue
                    Q.append(next)
    return True if sum(visited) == n else False



print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))
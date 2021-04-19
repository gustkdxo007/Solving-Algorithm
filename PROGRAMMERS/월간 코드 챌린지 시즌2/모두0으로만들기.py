import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    if sum(a) != 0: return -1
    answer = 0
    N = len(a)
    visited = [0] * N
    G = [[] for _ in range(N)]
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)

    def dfs(n):
        nonlocal answer
        total = a[n]
        visited[n] = 1
        for next in G[n]:
            if visited[next] == 1: continue
            tmp = dfs(next)
            answer += abs(tmp)
            total += tmp
        return total
    dfs(0)
    return answer




print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))
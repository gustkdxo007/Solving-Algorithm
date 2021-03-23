import sys
sys.stdin = open('../INPUT/1219.txt', 'r')

def dfs(v):
    global adj, visited
    # 목적지에 도착했거나, 이미 방문한 지점일 경우 실행하지 않음
    if v == 99:  # 경로를 찾음
        return 1
    if visited[v]:
        return 0
    visited[v] = 1
    #  현재 지점에서 도착할 수 있는 모든 지점에 대해서 진행
    result1 = result2 = 0
    if adj[0][v]:
        result1 = dfs(adj[0][v])
    if adj[1][v]:
        result2 = dfs(adj[1][v])

    return result1 or result2

# def dfs2():
#     global adj, visited
#     stack = list()
#     stack.append(0)
#
#     while stack:
#         v = stack.pop()  # 가장 최근에 추가된 정점 가져오기
#         visited[v] = 1
#         # 정점에서 갈 수 있는 모든 경로 진행
#         if adj[0][v] == 99 or adj[1][v] == 99:
#             return 1
#
#         if not visited[adj[0][v]]:  # 다음 경로를 방문하지 않았다면 추가
#             stack.append(adj[0][v])
#         if not visited[adj[1][v]]:
#             stack.append(adj[1][v])
#     return 0

T = 10
for _ in range(T):
    tc, N = map(int, input().split())
    result = 0
    path = [*map(int, input().split())]
    adj = [[0] * 100 for _ in range(2)]
    visited = [0]* 100
    for i in range(0, len(path), 2):
        if not adj[0][path[i]]:
            adj[0][path[i]] = path[i+1]
        else:
            adj[1][path[i]] = path[i+1]

    result = dfs(0)
    # result = dfs2()
    print('#{} {}'.format(tc, result))
# from collections import deque
# def solution(n, edge):
#     answer = 0
#     graph = [[] for _ in range(n+1)]
#     visited = [0] * (n+1)
#     for u, v in edge:
#         graph[u].append(v)
#         graph[v].append(u)
#     max_cnt = 0
#     def bfs(k):
#         nonlocal max_cnt
#         Q = deque()
#         Q.append((k, 1))
#         while Q:
#             node, cnt = Q.popleft()
#             if visited[node]: continue
#             visited[node] = cnt
#             max_cnt = max(max_cnt, cnt)
#             for g in graph[node]:
#                 Q.append((g, cnt+1))
#
#     bfs(1)
#     answer = visited.count(max_cnt)
#     print(answer)
#     return answer


3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1
    print(distances)
    distances.sort(reverse=True)
    answer = distances.count(distances[0])
    print(answer)
    return answer


solution(6, [[3,6], [4,3], [3,2], [1,3], [1,2], [2,4], [5,2]])
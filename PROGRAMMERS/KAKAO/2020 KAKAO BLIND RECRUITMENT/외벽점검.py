from itertools import permutations

def solution(n, weak, dist):
    answer = int(1e9)
    weak_point = weak + [w+n for w in weak]
    for i in range(len(weak)):
        for friends in permutations(dist):
            cnt = 1
            now = weak[i]
            for friend in friends:
                now += friend
                if now < weak_point[i+len(weak)-1]:
                    cnt += 1
                    now = [w for w in weak_point[i+1:i+len(weak)] if w > now][0]
                else:
                    answer = min(answer, cnt)
    return -1 if answer == int(1e9) else answer

# 다른 사람 풀이
# from collections import deque
#
# def solution(n, weak, dist):
#     dist.sort(reverse=True)
#     q = deque([weak])
#     visited = set()
#     visited.add(tuple(weak))
#     for i in range(len(dist)):
#         d = dist[i]
#         for _ in range(len(q)):
#             current = q.popleft()
#             for p in current:
#                 l = p
#                 r = (p + d) % n
#                 if l < r:
#                     temp = tuple(filter(lambda x: x < l or x > r, current))
#                 else:
#                     temp = tuple(filter(lambda x: x < l and x > r, current))
#
#                 if len(temp) == 0:
#                     return (i + 1)
#                 elif temp not in visited:
#                     visited.add(temp)
#                     q.append(list(temp))
#     return -1

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
import sys
sys.stdin = open('../INPUT/11000.txt')

import heapq

N = int(input())
time_table = [[*map(int, input().split())] for _ in range(N)]
time_table.sort()
end = [0]
for s, e in time_table:
    last = end[0]
    if s < last:
        heapq.heappush(end, e)
    else:
        heapq.heappop(end)
        heapq.heappush(end, e)
print(len(end))


# N = int(input())
# time_table = [[*map(int, input().split())] for _ in range(N)]
# time_table.sort()
# end = [0]
# for s, e in time_table:
#     last = min(end)
#     if s < last:
#         end.append(e)
#     else:
#         end.remove(last)
#         end.append(e)
# print(len(end))
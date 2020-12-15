import heapq
def solution(scoville, k):
    answer = 0
    Q = []
    for i in scoville:
        heapq.heappush(Q, i)
    while Q:
        f = heapq.heappop(Q)
        if f >= k: break
        if not Q:
            answer = -1
            break
        s = heapq.heappop(Q)
        heapq.heappush(Q, f+s*2)
        answer += 1
    return answer

print(solution([1,2,3,9,10,12], 7))
import heapq

def solution(jobs):
    answer = []
    Q = []
    for i in range(len(jobs)):
        heapq.heappush(Q, jobs[i])
    now = 0
    while Q:
        waited = []
        while Q and Q[0][0] <= now:
            waited.append(heapq.heappop(Q))
        waited.sort(key=lambda x: (x[1], x[0]))
        if waited:
            for i in range(len(waited)):
                if i == 0:
                    answer.append(now-waited[i][0]+waited[i][1])
                    now += waited[i][1]
                else:
                    heapq.heappush(Q, waited[i])
        else:
            now += 1

    return sum(answer) // len(answer)


print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]))
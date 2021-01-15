import bisect

def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[0], x[1]))
    departures = [x[0] for x in tickets]
    visited = [0] * len(tickets)

    def dfs(dep, res):
        if len(res) == len(tickets)+1:
            answer.append([x for x in res])
            return
        s = bisect.bisect_left(departures, dep)
        e = bisect.bisect_right(departures, dep)
        for i in range(s, e):
            if visited[i]: continue
            visited[i] = 1
            res.append(tickets[i][1])
            dfs(tickets[i][1], res)
            res.pop()
            visited[i] = 0
    dfs('ICN', ['ICN'])

    return answer[0]



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
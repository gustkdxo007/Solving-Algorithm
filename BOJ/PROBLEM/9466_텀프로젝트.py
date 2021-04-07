import sys
sys.stdin = open("../INPUT/9466.txt")
sys.setrecursionlimit(1000000)

def find_team(n, team):
    visited[n] = 1
    team.append(n)
    friend = friends[n]

    if not visited[friend]:
        find_team(friend, team)
    else:
        if friend in team:
            while team_check[friend] != -1:
                team_check[friend] = -1
                friend = friends[friend]


T = int(input())
for t in range(T):
    N = int(input())
    friends = [0] + [*map(int, input().split())]
    visited = [0] * (N + 1)
    team_check = [-1] + [0] * N
    for i in range(1, N+1):
        if visited[i]: continue
        find_team(i, [])
    print(team_check.count(0))

def solution(n, costs):
    answer = 0
    parent = [x for x in range(n+1)]
    costs.sort(key=lambda x: x[2])

    def find_parent(x, parent):
        if parent[x] != x:
            parent[x] = find_parent(parent[x], parent)
        return parent[x]

    def union(a, b, parent):
        x = find_parent(a, parent)
        y = find_parent(b, parent)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    for s, t, c in costs:
        if find_parent(s, parent) != find_parent(t, parent):
            answer += c
            union(s, t, parent)
    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
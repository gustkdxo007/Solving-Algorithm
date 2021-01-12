def solution(citations):
    citations.sort()
    N = len(citations)
    for i in range(N, -1, -1):
        for j in range(N):
            if citations[j] >= i:
                if N - j >= i:
                    return i
                else:
                    break
    # citations.sort(reverse=True)
    # print(max(map(min, enumerate(citations, start=1))))

print(solution([3, 0, 6, 1, 5]))
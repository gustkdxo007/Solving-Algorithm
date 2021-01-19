def solution(genres, plays):
    answer = []
    N = len(genres)
    countByGenres = dict()
    zipForGenres = dict()

    for i in range(N):
        if genres[i] in countByGenres:
            countByGenres[genres[i]] += plays[i]
        else:
            countByGenres[genres[i]] = plays[i]
        if genres[i] in zipForGenres:
            zipForGenres[genres[i]].append((plays[i], i))
        else:
            zipForGenres[genres[i]] = [(plays[i], i)]
    orderedGenre = sorted(countByGenres, key=lambda x: countByGenres[x], reverse=True)
    for g in orderedGenre:
        zipForGenres[g].sort(key=lambda x: (-x[0], [1]))
        for i in zipForGenres[g][:2]:
            answer.append(i[1])
    return answer


print(solution(["classic",  "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic","classic","classic","classic","pop"], [500,150,800,800,2500]))
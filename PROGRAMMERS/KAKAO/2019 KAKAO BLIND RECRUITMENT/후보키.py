from itertools import combinations

def solution(relation):
    N = len(relation)
    M = len(relation[0])
    candidate = []
    for i in range(1, N+1):
        for comb in combinations([x for x in range(M)], i):
            tmp_set = set()
            for j in range(N):
                tmp_comb = []
                for c in comb:
                    tmp_comb.append(relation[j][c])
                tmp_set.add(tuple(tmp_comb))
            if len(tmp_set) == N:
                candidate.append(set(comb))

    del_set = set()
    for elem in candidate:
        for elem2 in candidate:
            if elem.issubset(elem2) and elem != elem2:
                del_set.add(tuple(elem2))
    return len(candidate) - len(del_set)



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
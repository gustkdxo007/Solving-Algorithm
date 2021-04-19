def solution(a):
    answer = 0
    e_idx = dict()
    for i in range(len(a)):
        if a[i] in e_idx:
            e_idx[a[i]].append(i)
        else:
            e_idx[a[i]] = [i]
    for e, arr in sorted(e_idx.items(), reverse=True, key=lambda x : len(x[1])):
        last = -1
        cnt = 0
        if len(arr) <= answer // 2: continue
        for i in arr:
            if i - 1 >= 0 and a[i-1] != e and last != i-1:
                cnt += 2
                last = i-1
            elif i + 1 < len(a) and a[i+1] != e and last != i+1:
                cnt += 2
                last = i+1
        answer = max(answer, cnt)
    return answer


print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))
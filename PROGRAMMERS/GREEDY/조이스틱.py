def solution(name):
    answer = 0
    name_cnt = [0] * len(name)
    for n in range(len(name)):
         name_cnt[n] = min(ord(name[n])-65, 91-ord(name[n]))
    idx = 0
    while True:
        answer += name_cnt[idx]
        name_cnt[idx] = 0
        if sum(name_cnt) == 0: break
        left = right = 1
        while name_cnt[idx-left] == 0:
            left += 1
        while name_cnt[idx+right] == 0:
            right += 1
        answer += left if left < right else right
        idx += (-left) if left < right else right
    return answer

print(solution("JAZ"))
print(solution("JEROEN"))
print(solution("JAN"))
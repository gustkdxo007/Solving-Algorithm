def solution(n, t, m, p):
    answer = ''
    notation = '0123456789ABCDEF'
    cache = {}
    game = ''
    def conversion(num, base):
        if num in cache:
            return cache[num]
        q, r = divmod(num, base)
        l = notation[r]
        cache[num] = conversion(q, base) + l if q else l
        return cache[num]
    cnt = 0
    while len(game) <= t * m:
        game += conversion(cnt, n)
        cnt += 1
    for i in range(0, len(game), m):
        answer += game[i+p-1]
        if len(answer) == t: break
    return answer


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
def solution(n, cores):
    N = len(cores)
    if n <= N:
        return n
    min_time = min(cores)
    left = (n // N) * min_time
    right = n * min_time

    while left <= right:
        mid = (left + right) // 2
        cnt = N
        now_work = 0
        for i in range(N):
            cnt += (mid // cores[i])
            if mid % cores[i] == 0:
                now_work += 1

        if cnt < n:
            left = mid + 1
        elif cnt - now_work >= n:
            right = mid - 1
        else:
            cnt -= now_work
            for i in range(N):
                if mid % cores[i] == 0:
                    cnt += 1
                if cnt == n:
                    return i + 1


print(solution(6, [1,2,3]))
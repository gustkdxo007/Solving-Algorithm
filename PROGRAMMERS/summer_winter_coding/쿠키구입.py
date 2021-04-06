def solution(cookie):
    N = len(cookie)
    answer = 0
    for i in range(N-1):
        left_idx, right_idx = i, i+1
        left_sum, right_sum = cookie[left_idx], cookie[right_idx]
        while left_idx >= 0 or right_idx < N:
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                left_idx -= 1
                if left_idx < 0: break
                left_sum += cookie[left_idx]
            elif left_sum < right_sum:
                left_idx -= 1
                if left_idx < 0: break
                left_sum += cookie[left_idx]
            else:
                right_idx += 1
                if right_idx >= N: break
                right_sum += cookie[right_idx]
    return answer


print(solution([1,1,2,3]))
print(solution([1,2,4,5]))
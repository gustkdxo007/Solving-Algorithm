import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    Q = []
    length = len(food_times)
    for i in range(length):
        heapq.heappush(Q, (food_times[i], i))

    sum_value = 0
    previous = 0

    while sum_value + (Q[0][0] - previous) * length <= k:
        now = heapq.heappop(Q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now
    result = sorted(Q, key=lambda x: x[1])
    return result[(k-sum_value) % length][1]+1

print(solution([3, 1, 2], 5))
print(solution([8, 6, 4], 15))
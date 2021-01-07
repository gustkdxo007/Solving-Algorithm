def solution(n, stations, w):
    answer = 0
    right = 0
    for i in range(len(stations)):
        if i == 0:
            left = stations[i] - w - 1
            if left > 0:
                answer += (left - 1) // (2 * w + 1) + 1
            right = stations[i] + w
        if i + 1 < len(stations):
            a = right + 1
            b = stations[i+1] - w - 1
            if b - a >= 0:
                answer += (b - a) // (2 * w + 1) + 1
            right = stations[i+1] + w
            if right >= n:
                return answer
        else:
            a = right + 1
            b = n
            answer += (b - a) // (2 * w + 1) + 1
    return answer

print(solution(11, [4, 9], 1))
print(solution(16, [13,16], 2))
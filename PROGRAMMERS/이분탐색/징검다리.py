def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    while left <= right:
        prev = 0
        mid = (left + right) // 2
        removed_rock = 0
        min_distance = 1000000001
        for rock in rocks:
            if rock - prev < mid:
                removed_rock += 1
            else:
                min_distance = min(min_distance, rock-prev)
                prev = rock
            if removed_rock > n: break

        if removed_rock > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = min_distance
    return answer



print(solution(25, [2, 14, 11, 21, 17], 2))
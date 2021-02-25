from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            if cache[-1] != city:
                cache.remove(city)
                cache.append(city)
        else:
            answer += 5
            if len(cache) == cacheSize and cache:
                cache.popleft()
            if len(cache) < cacheSize:
                cache.append(city)
    return answer



print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']))
print(solution(2, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))
print(solution(2, ['Jeju', 'Pangyo', 'NewYork', 'newyork']))
print(solution(0, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
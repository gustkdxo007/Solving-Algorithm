import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = collections.deque([0]*bridge_length)
    truck_weights = truck_weights[::-1]
    sum_ = 0
    while bridge:
        answer += 1
        passed = bridge.popleft()
        if passed:
            sum_ -= passed
        if truck_weights:
            if sum_ + truck_weights[len(truck_weights)-1] <= weight:
                w = truck_weights.pop()
                bridge.append(w)
                sum_ += w
            else:
                bridge.append(0)
    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
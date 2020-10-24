def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)):
        passed = i+1
        check = True
        while passed < len(prices):
            if prices[passed] < prices[i]:
                answer[i] = passed - i
                check = False
                break
            passed += 1
        if check:
            answer[i] = passed-1-i
    return answer

print(solution([1,2,3,2,3]))
def solution(routes):
    answer = 1
    routes.sort()
    tmp = routes[0][1]
    for i in range(len(routes)-1):
        if tmp > routes[i][1]:
            tmp = routes[i][1]
        if tmp < routes[i+1][0]:
            answer += 1
            tmp = routes[i+1][1]
    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))
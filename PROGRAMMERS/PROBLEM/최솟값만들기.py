# def solution(a, b):
#     answer = 0
#     a.sort()
#     b.sort(reverse=True)
#     for i in range(len(a)):
#         answer += a[i]*b[i]
#     return answer

def solution(a, b):
    return sum(map(lambda a,b: a * b, sorted(a), sorted(b, reverse=True)))


print(solution([1,4,2], [5,4,4]))
print(solution([1,2], [3,4]))
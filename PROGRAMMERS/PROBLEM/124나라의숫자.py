def solution(n):
    answer = ''
    num = [1, 2, 4]
    while n:
        q, r = (n-1) // 3, (n-1) % 3
        answer += str(num[r])
        n = q
    return answer[::-1]

# def solution(n):
#     answer = ''
#     p = [1, 2, 4]
#     arr = []
#     while n:
#         q, r = divmod(n-1, 3)
#         arr.append(p[r])
#         n = q
#     print(arr)
#     for i in range(len(arr)-1, -1, -1):
#         answer += str(arr[i])
#     return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(7))
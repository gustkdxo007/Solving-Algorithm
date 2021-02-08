def solution(s):
    input_array = [*map(int, s.split(" "))]
    input_array.sort()
    return str(input_array[0]) + ' ' + str(input_array[-1])


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
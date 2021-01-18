def solution(operations):
    arr = []
    for oper in operations:
        d, n = oper.split()
        if d == 'I':
            arr.append(int(n))
            arr.sort()
        else:
            if arr and n == '1':
                del arr[len(arr)-1]
            elif arr and n == '-1':
                del arr[0]
    if arr:
        return [arr[len(arr)-1], arr[0]]
    else:
        return [0, 0]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
def check_zip(r1, r2, c1, c2, arr):
    check = arr[r1][c1]
    for i in range(r1, r2):
        for j in range(c1, c2):
            if arr[i][j] != check:
                return False
    return True

def zip(r, c, n, arr, answer):
    if check_zip(r, r+n, c, c+n, arr):
        answer[arr[r][c]] += 1
    else:
        zip(r, c, n//2, arr, answer)
        zip(r+n//2, c, n//2, arr, answer)
        zip(r, c+n//2, n//2, arr, answer)
        zip(r+n//2, c+n//2, n//2, arr, answer)
    return answer

def solution(arr):
    answer = [0, 0]
    N = len(arr)


    return zip(0, 0, N, arr, [0, 0])

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
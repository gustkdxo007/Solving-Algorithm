def solution(n):
    answer = []
    maps = [[0]* n for _ in range(n)]
    y, x = -1, 0
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            maps[y][x] = number
            number += 1
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 0: continue
            answer.append(maps[i][j])
    return answer

solution(4)
solution(5)
solution(6)
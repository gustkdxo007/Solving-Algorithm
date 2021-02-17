def solution(dirs):
    dist = set()
    x = y = 0
    for d in dirs:
        if d == 'L':
            dx, dy = x-1, y
        elif d == 'U':
            dx, dy = x, y-1
        elif d == 'R':
            dx, dy = x+1, y
        elif d == 'D':
            dx, dy = x, y+1
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            if (dx, dy, x, y) not in dist:
                dist.add((x, y, dx, dy))
            x, y = dx, dy
    return len(dist)



print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution('UDU'))
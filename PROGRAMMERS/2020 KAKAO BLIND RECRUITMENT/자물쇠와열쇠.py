def solution(key, lock):
    plus_size = (len(key)-1) * 2
    matrix = [[0]*(plus_size+len(lock)) for _ in range(plus_size+len(lock))]
    cnt = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            matrix[i+len(key)-1][j+len(key)-1] = lock[i][j]
            if not lock[i][j]:
                cnt += 1
    def is_fit_lock():
        for i in range(len(key) - 1 + len(lock)):
            for j in range(len(key) - 1 + len(lock)):
                tmp_cnt = cnt
                check = True
                for ii in range(len(key)):
                    for jj in range(len(key)):
                        if i+ii < len(key)-1 or i+ii >= len(key)-1+len(lock) or j+jj < len(key)-1 or j+jj >= len(key)-1+len(lock): continue
                        if not key[ii][jj]: continue
                        if key[ii][jj] == matrix[i+ii][j+jj]:
                            check = False
                            continue
                        else:
                            tmp_cnt -= 1
                if not tmp_cnt and check:
                    return True
        return False

    def rotate_key():
        tmp_key = [[0]*len(key) for _ in range(len(key))]
        for i in range(len(key)):
            for j in range(len(key)):
                tmp_key[j][len(key)-1-i] = key[i][j]
        return tmp_key

    for r in range(4):
        if is_fit_lock():
            return True
        else:
            key = rotate_key()
    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]], [[1,1,1],[1,1,0],[1,0,1]]))
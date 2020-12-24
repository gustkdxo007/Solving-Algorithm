def is_solution(answer):
    for x, y, a in answer:
        if a:
            # 보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer): continue
            return False
            pass
        else:
            # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer: continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b:
            #설치
            answer.append([x, y, a])
            if not is_solution(answer):
                answer.remove([x, y, a])
        else:
            #삭제
            answer.remove([x, y, a])
            if not is_solution(answer):
                answer.append([x, y, a])
    answer.sort(key=lambda x:(x[0], x[1], x[2]))
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
def solution(msg):
    answer = []
    zip = { 'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
            'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
            'X': 24, 'Y': 25, 'Z': 26 }
    idx = 0
    while idx < len(msg):
        tmp = msg[idx]
        if tmp in zip:
            tmp_c = tmp
            tmp_idx = idx
            while tmp_c in zip:
                tmp_idx += 1
                if tmp_idx >= len(msg): break
                tmp_c += msg[tmp_idx]
            if tmp_idx >= len(msg):
                answer.append(zip[tmp_c])
            else:
                answer.append(zip[tmp_c[:-1]])
                zip[tmp_c] = len(zip) + 1
            idx = tmp_idx
    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
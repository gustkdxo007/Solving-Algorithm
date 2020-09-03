def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        compressed_str = ""
        cnt = 0
        string = s[:i]
        for j in range(0, len(s), i):
            divided = s[j:j + i]
            if string == divided:
                cnt += 1
            else:
                if cnt > 1:
                    compressed_str += (str(cnt) + string)
                else:
                    compressed_str += string
                cnt = 1
                string = divided
        if cnt > 1:
            compressed_str += (str(cnt) + divided)
        elif cnt == 1:
            compressed_str += divided
        if answer > len(compressed_str):
            answer = len(compressed_str)

    return answer

INPUT = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]
for i in INPUT:
    print(solution(i))
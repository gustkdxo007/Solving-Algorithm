def solution(words):
    answer = 0
    words.sort()
    def compareTwoWords(prev, now):
        for i in range(1, len(now) + 1):
            if prev[:i] != now[:i]:
                return i
        return i

    def compareThreeWords(prev, now, next):
        for i in range(1, len(now) + 1):
            if prev[:i] != now[:i] and now[:i] != next[:i]:
                return i
        return i

    for i in range(len(words)):
        if i == 0:
            answer += compareTwoWords(words[i+1], words[i])
        elif i == len(words)-1:
            answer += compareTwoWords(words[i-1], words[i])
        else:
            answer += compareThreeWords(words[i-1], words[i], words[i+1])
    return answer


print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]))
import bisect

def get_cnt(arr, l, r):
    left_idx = bisect.bisect_left(arr, l)
    right_idx = bisect.bisect_right(arr, r)
    return right_idx - left_idx

def solution(words, queries):
    answer = []
    lengthByWord = dict()
    reversed_lengthByWord = dict()
    for word in words:
        if len(word) in lengthByWord:
            lengthByWord[len(word)].append(word)
            reversed_lengthByWord[len(word)].append(word[::-1])
        else:
            lengthByWord[len(word)] = [word]
            reversed_lengthByWord[len(word)] = [word[::-1]]
    for ln in lengthByWord:
        lengthByWord[ln].sort()
        reversed_lengthByWord[ln].sort()
    for q in queries:
        if q[-1] == '?':
            if lengthByWord.get(len(q)):
                answer.append(get_cnt(lengthByWord.get(len(q)), q, q.replace('?', 'z')))
            else:
                answer.append(0)
        else:
            if lengthByWord.get(len(q)):
                answer.append(get_cnt(reversed_lengthByWord[len(q)], q[::-1], q[::-1].replace('?', 'z')))
            else:
                answer.append(0)


    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

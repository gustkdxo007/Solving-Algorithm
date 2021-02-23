def solution(n, words):
    answer = [0, 0]
    N = len(words) // n + 1 if len(words) % n else len(words) // n
    for i in range(N):
        for j in range(n):
            if i == 0 and j == 0: continue
            if i * n + j >= len(words): break
            if words[i * n + j - 1][-1] != words[i * n + j][0] or words.index(words[i * n + j]) != i * n + j:
                answer[0], answer[1] = j + 1, i + 1
                return answer
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
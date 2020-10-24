def countPerms(n):
    # Write your code here
    vowel = [0] * 5
    for i in range(n):
        tmp_vowel = [0] * 5
        if i == 0:
            vowel = [1] * 5
            continue
        if vowel[0]:
            tmp_vowel[1] += vowel[0]
        if vowel[1]:
            tmp_vowel[0] += vowel[1]
            tmp_vowel[2] += vowel[1]
        if vowel[2]:
            tmp_vowel[0] += vowel[2]
            tmp_vowel[1] += vowel[2]
            tmp_vowel[3] += vowel[2]
            tmp_vowel[4] += vowel[2]
        if vowel[3]:
            tmp_vowel[2] += vowel[3]
            tmp_vowel[4] += vowel[3]
        if vowel[4]:
            tmp_vowel[0] += vowel[4]
        vowel = tmp_vowel[:]
    return sum(vowel) % (10**9+7)

print(countPerms(3))


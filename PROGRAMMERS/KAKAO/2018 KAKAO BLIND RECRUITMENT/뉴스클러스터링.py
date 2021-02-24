def make_set(str):
    tmp_set = []
    for i in range(1, len(str)):
        if 97 <= ord(str[i-1]) <= 122 and 97 <= ord(str[i]) <= 122:
            tmp_set.append(str[i-1] + str[i])
    return tmp_set

def solution(str1, str2):
    A, B = 0, 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = make_set(str1)
    str2_set = make_set(str2)
    union = set(str1_set) | set(str2_set)
    for str in list(union):
        a, b = str1_set.count(str), str2_set.count(str)
        A += min(a, b)
        B += max(a, b)
    if A == 0 and B == 0:
        return 65536
    return int(A / B * 65536)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
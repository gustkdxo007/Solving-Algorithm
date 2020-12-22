import sys
sys.stdin = open('../INPUT/문자열재정렬.txt', 'r')

T = int(input())
for t in range(T):
    S = input()
    result = []
    num = 0
    for s in S:
        if s.isalpha():
            result.append(s)
        else:
            num += int(s)
    result.sort()
    if num:
        result.append(str(num))
    print(''.join(result))
import sys
sys.stdin = open('../INPUT/문자열압축.txt', 'r')

T = int(input())
for t in range(T):
    S = input()
    result = len(S)
    for i in range(1, len(S)//2+1):
        tmp = ''
        prev = S[:i]
        cnt = 1
        for j in range(i, len(S), i):
            if prev == S[j:j+i]:
                cnt += 1
            else:
                tmp += str(cnt) + prev if cnt >= 2 else prev
                prev = S[j:j+i]
                cnt = 1
        tmp += str(cnt) + prev if cnt >= 2 else prev
        result = min(result, len(tmp))
    print(result)
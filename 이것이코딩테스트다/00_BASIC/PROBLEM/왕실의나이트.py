import sys
sys.stdin = open('../INPUT/왕실의나이트.txt', 'r')

T = int(input())
D = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)]
for t in range(T):
    input_data = input()
    r = int(input_data[1])
    c = ord(input_data[0]) - ord('a') + 1
    result = 0
    for d in D:
        dr, dc = r+d[0], c+d[1]
        if dr < 1 or dr > 8 or dc < 1 or dc > 8: continue
        result += 1
    print(result)

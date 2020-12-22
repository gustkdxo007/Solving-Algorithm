import sys
sys.stdin = open('../INPUT/럭키스트레이트.txt', 'r')

T = int(input())
for t in range(T):
    input_number = [*map(int, list(input()))]
    n = len(input_number) // 2
    print('LUCKY') if sum(input_number[:n]) == sum(input_number[n:]) else print('READY')
import sys
sys.stdin = open("../INPUT/숫자카드게임.txt", "r")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    cards = [[*map(int, input().split())] for _ in range(N)]
    result = 0
    for card in cards:
        result = max(result, min(card))
    print(result)
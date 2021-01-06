import sys
sys.stdin = open('../INPUT/안테나.txt', 'r')

N = int(input())
position = [*map(int, input().split())]
position.sort()
print(position[(N-1)//2])
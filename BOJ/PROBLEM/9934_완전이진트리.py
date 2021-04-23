import sys
sys.stdin = open("../INPUT/9934.txt", "r")

K = int(input())
visited = [*map(int, input().split())]
tree = [[] for _ in range(K)]

def make_tree(s, e, k):
    if k == K:
        return
    mid = (s+e) // 2
    tree[k].append(visited[mid])
    make_tree(s, mid-1, k+1)
    make_tree(mid+1, e, k+1)
make_tree(0, len(visited), 0)
for t in tree:
    print(*t)


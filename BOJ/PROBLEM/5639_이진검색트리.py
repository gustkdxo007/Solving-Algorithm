import sys
sys.stdin = open("../INPUT/5639.txt", "r")
sys.setrecursionlimit(1000000)

pre_order = []
while True:
    try:
        node = int(input())
    except: break
    pre_order.append(node)

def post_order(s, e):
    if s >= e:
        return
    div = e
    for i in range(s+1, e):
        if pre_order[s] < pre_order[i]:
            div = i
            break
    post_order(s+1, div)
    post_order(div, e)
    print(pre_order[s])

post_order(0, len(pre_order))
from sys import setrecursionlimit
import heapq

setrecursionlimit(10000)

def solution(nodeinfo):
    Q = []
    preOrder = []
    postOrder = []
    for i in range(len(nodeinfo)):
        heapq.heappush(Q, (-nodeinfo[i][1], nodeinfo[i][0], i+1))
    N = len(nodeinfo)
    L = [0] * (N+1)
    R = [0] * (N+1)
    P = [0] * (N+1)
    location = [0] * (N+1)
    root = 0
    while Q:
        y, x, n = heapq.heappop(Q)
        y *= -1
        location[n] = (x, y)
        if not root:
            root = n
            continue
        current = root
        while True:
            if x < location[current][0]:
                if L[current]:
                    current = L[current]
                    continue
                else:
                    L[current] = n
                    P[n] = current
                    break
            elif x > location[current][0]:
                if R[current]:
                    current = R[current]
                    continue
                else:
                    R[current] = n
                    P[n] = current
                    break
            break

    def make_preorder(node):
        preOrder.append(node)
        if L[node]:
            make_preorder(L[node])
        if R[node]:
            make_preorder(R[node])

    def make_postorder(node):
        if L[node]:
            make_postorder(L[node])
        if R[node]:
            make_postorder(R[node])
        postOrder.append(node)

    make_preorder(root)
    make_postorder(root)

    return [preOrder, postOrder]


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
import sys
sys.stdin = open("../INPUT/1991.txt", "r")

N = int(input())
tree = [[0]* 3 for _ in range(N)]
for _ in range(N):
    root, left, right = input().split()
    root_idx = ord(root) - 65
    tree[root_idx][0], tree[root_idx][1], tree[root_idx][2] = root, left, right

def preorder(s):
    print(s, end="")
    node_idx = ord(s) - 65
    if tree[node_idx][1] != ".":
        preorder(tree[node_idx][1])
    if tree[node_idx][2] != ".":
        preorder(tree[node_idx][2])

def inorder(s):
    node_idx = ord(s) - 65
    if tree[node_idx][1] != ".":
        inorder(tree[node_idx][1])
    print(s, end="")
    if tree[node_idx][2] != ".":
        inorder(tree[node_idx][2])

def postorder(s):
    node_idx = ord(s) - 65
    if tree[node_idx][1] != ".":
        postorder(tree[node_idx][1])
    if tree[node_idx][2] != ".":
        postorder(tree[node_idx][2])
    print(s, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
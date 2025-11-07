from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    #this fucntion will ensure that whenever we peint an instance of Node class it will print the value.
    def __str__(self):
        return str(self.val)


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

print(A)

#DFS has 3 kinds of orders preorder, inorder, postorder
# All of them take O(n) space, O(n) time
def dfs_pre(node):
    if not node:
        return
    if not isinstance(node,Node):
        return
    print(node)
    dfs_pre(node.left)
    dfs_pre(node.right)

def dfs_post(node):
    if not node:
        return
    if not isinstance(node,Node):
        return
    dfs_post(node.left)
    dfs_post(node.right)
    print(node)

def dfs_in(node):
    if not node:
        return
    if not isinstance(node,Node):
        return
    dfs_in(node.left)
    print(node)
    dfs_in(node.right)

# DFS can only be done in pre-order if done iteratively, bacause the positioning
# of the print statement does not matter.

def dfs_pre_stack(node):
    stk = [node]
    while stk:
        node = stk.pop()
        print(node)
        if node.right:
            stk.append(node.right)
        if node.left:
            stk.append(node.left)


def bfs_trversal(node):
    q= deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


# Searching for a value:
def search_bi_tree(node,t):
    if not node:
        return False
    if not isinstance(node, Node):
        return False

    if node.val == t:
        return True

    return search_bi_tree(node.left, t) or search_bi_tree(node.right, t)


print("DFS in preorder is:")
dfs_pre(A)

print("DFS in inorder is:")
dfs_in(A)

print("DFS in postorder is:")
dfs_post(A)

print("DFS in preorder with stack is:")
dfs_pre_stack(A)

print("BFS traversal of tree:")
bfs_trversal(A)

print("Is -1 in the tree:")
print(str(search_bi_tree(A,-1)))
print("Is 4 in the tree:")
print(str(search_bi_tree(A,4)))


print("BINARY SEARCH TREES")

# Binary Search Trees (BSTs)

#       5
#    1    8
#  -1 3  7 9

A2 = Node(5)
B2 = Node(1)
C2 = Node(8)
D2 = Node(-1)
E2 = Node(3)
F2 = Node(7)
G2 = Node(9)

A2.left, A2.right = B2, C2
B2.left, B2.right = D2, E2
C2.left, C2.right = F2, G2

print(A2)

def search_bst(node, t):
    if not node:
        return False
    if not isinstance(node,Node):
        return False
    if node.val == t:
        return True
    elif t < node.val:
        return search_bst(node.left, t)
    else:
        return search_bst(node.right, t)

print(f"Is -1 in the tree?: {search_bst(A2, -1)}")
print(f"Is 99 in the tree?: {search_bst(A2, 99)}")

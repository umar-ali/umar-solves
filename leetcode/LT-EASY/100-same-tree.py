from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root:Optional[TreeNode]) -> list[int]:
    l = []
    q = deque([root])
    while q:
        p = q.popleft()
        if p is not None:
            l.append(p.val)
            q.append(p.left)
            q.append(p.right)
    return l

def traverse_in_order(root:Optional[TreeNode], ordered = []):
    if root:
        traverse_in_order(root.left, ordered)
        ordered.append(root.val)
        traverse_in_order(root.right, ordered)
    return

def isSameTree(p:Optional[TreeNode], q:Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    #pre-order recursive
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def inorderTraversal(root:Optional[TreeNode]) -> list[int]:
    l = []
    if root:
        traverse_in_order(root, l)
    return l


def build_tree_inorder(elems) -> Optional[TreeNode]:
    if len(elems) == 0:
        return None
    head_elem = elems[0]
    if head_elem is None:
        return None
        
    head = TreeNode(head_elem)
    q = deque([head])
    i = 1
    while i < len(elems):
        p = q.popleft()

        l = None
        if elems[i] is not None:
            l = TreeNode(elems[i])
            q.append(l)
        p.left = l

        if i+1 == len(elems):
            break

        r = None
        if elems[i+1] is not None:
            r = TreeNode(elems[i+1])
            q.append(r)

        p.right = r
        i += 2
    return head

if __name__ == "__main__":
    rl1 = [1,2,3,4,5, None,8, None, None,6,7,9]
    rl2 = [1,2,3,4,11, None,8, None, None,6,7,9]
    tr1 = build_tree_inorder(rl1)
    tr2 = build_tree_inorder(rl2)
    print(isSameTree(tr1, tr2))


    rl1 = [None]
    rl2 = [None]
    tr1 = build_tree_inorder(rl1)
    tr2 = build_tree_inorder(rl2)
    print(isSameTree(tr1, tr2))

    rl1 = [1, 2]
    rl2 = [2, 1]
    tr1 = build_tree_inorder(rl1)
    tr2 = build_tree_inorder(rl2)
    print(isSameTree(tr1, tr2))


    rl1 = [1, None, 2]
    rl2 = [1, 2]
    tr1 = build_tree_inorder(rl1)
    tr2 = build_tree_inorder(rl2)
    print(isSameTree(tr1, tr2))
    # print(inorderTraversal(r))

    # rl = [1]
    # r = build_tree_inorder(rl)
    # print(inorderTraversal(r))

    # rl = [None]
    # r = build_tree_inorder(rl)
    # print(inorderTraversal(r))

    # rl = [1, 2, None, 3]
    # r = build_tree_inorder(rl)
    # print(inorderTraversal(r))







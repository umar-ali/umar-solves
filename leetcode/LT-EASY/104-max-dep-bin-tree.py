from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

def traverse_in_order(root:Optional[TreeNode], ordered = []):
    if root:
        traverse_in_order(root.left, ordered)
        ordered.append(root.val)
        traverse_in_order(root.right, ordered)
    return

def inorderTraversal(root:Optional[TreeNode]) -> list[int]:
    l = []
    if root:
        traverse_in_order(root, l)
    return l

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


def maxDepth( root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    elif root.left is None and root.right is None:
        return 1
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == "__main__":

    _in = [3, 9, 20, None, None, 15, 7]
    r1 = build_tree_inorder(_in)
    print(maxDepth(r1))









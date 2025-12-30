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

def height( root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    l = height(root.left)
    r = height(root.right)
    if l == -1 or r == -1 or abs(l - r) > 1:
        return -1
    return 1 + max(l, r)

def isBalanced(root: Optional[TreeNode]) -> bool:
    return height(root) > -1


if __name__ == "__main__":
    r = [3,9,20, None, None,15,7]
    print(isBalanced(build_tree_inorder(r)))

    

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root:Optional[TreeNode]) -> list[int]:
    l = []
    if root is not None:
        postorder(root, l)
    return l


def postorder(root:Optional[TreeNode], ordered = []) -> None: 
    if root is None:
        return None
    postorder(root.left, ordered)
    postorder(root.right, ordered)
    ordered.append(root.val)


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
    rl = [1,2,3,4,5, None,8, None, None,6,7,9]
    r = build_tree_inorder(rl)
    print(postorderTraversal(r))

    rl = [1]
    r = build_tree_inorder(rl)
    print(postorderTraversal(r))

    rl = [None]
    r = build_tree_inorder(rl)
    print(postorderTraversal(r))

    rl = [1, 2, None, 3]
    r = build_tree_inorder(rl)
    print(postorderTraversal(r))



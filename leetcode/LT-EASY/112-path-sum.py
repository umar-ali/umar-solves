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

def _has_path_sum(root:TreeNode, targetSum:int, currSum:int | None = None) -> bool:

    #only leaf node allowed
    # if root is None:
    #     return currSum is not None and  currSum == targetSum
    print(root.val, currSum, end=" ")
    currSum = currSum + root.val if currSum is not None else root.val
    print(currSum)

    if root.left is None and root.right is None:
        return currSum is not None and  currSum == targetSum

    lHas = False
    rHas = False

    if root.left is not None:
        lHas = _has_path_sum(root.left, targetSum=targetSum, currSum=currSum)
    
    if root.right is not None:
        rHas = _has_path_sum(root.right , targetSum=targetSum, currSum=currSum)
    
    return lHas or rHas

def hasPathSum(root:Optional[TreeNode], targetSum:int) -> bool:
    if root is None:
        return False
    return _has_path_sum(root=root, targetSum=targetSum)


if __name__ == "__main__":
    r1 =  [5,4,8,11, None,13,4,7,2, None, None, None,1]
    print(hasPathSum(build_tree_inorder(r1), 22))
    print("-"*50)
    r2 = [1,2,3]
    print(hasPathSum(build_tree_inorder(r2), 0))
    print("-"*50)
    r3 = []
    print(hasPathSum(build_tree_inorder(r3), 0))
    print("-"*50)
    r4 = [1, 2]
    print(hasPathSum(build_tree_inorder(r4), 1))
    print("-"*50)


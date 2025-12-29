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



def sortedArrayToBST(nums:list[int]) -> TreeNode | None:
    ln = len(nums)
    if ln == 0:
        return None
    mid = ln // 2 
    return TreeNode(val=nums[mid], left=sortedArrayToBST(nums[:mid]), right=sortedArrayToBST(nums[mid+1:]))

if __name__ == "__main__":
    i1 = []
    print(preorderTraversal(sortedArrayToBST(i1)))
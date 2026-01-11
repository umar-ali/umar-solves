from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root:Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    if root.left is None and root.right is None:
        return 1

    lh = minDepth(root.right)
    rh = minDepth(root.left)

    if lh == 0 or rh ==0:
        return 1 + max(lh, rh)
   
    return 1 + min(lh, rh)

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


def minDepth2(root):
    # Corner Case
    if root is None:
         return 0 

    # Create an empty queue for level order traversal
    q = []
    
    # Enqueue root and initialize depth as 1
    q.append({'node': root , 'depth' : 1})

    # Do level order traversal
    while(len(q)>0):
        # Remove the front queue item
        queueItem = q.pop(0)
    
        # Get details of the removed item
        node = queueItem['node']
        depth = queueItem['depth']
        # If this is the first leaf node seen so far
        # then return its depth as answer
        if node.left is None and node.right is None:    
            return depth 
        
        # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append({'node' : node.left , 'depth' : depth+1})

        # if right subtree is not None, add it to queue
        if node.right is not None:  
            q.append({'node': node.right , 'depth' : depth+1})


if __name__ == "__main__":
    inp = [3,9,20, None, None,15,7]
    print(minDepth(build_tree_inorder(inp)))
    inp2 =[2, None ,3, None,4, None,5, None,6]
    print(minDepth(build_tree_inorder(inp2)))
    inp3 =[2]
    print(minDepth(build_tree_inorder(inp3)))
    inp4=[]
    print(minDepth(build_tree_inorder(inp4)))
    inp5 = [-9,-3,2,None ,4,4,0,-6, None,-5]
    print(minDepth(build_tree_inorder(inp5)))
    inp5 = [-9,-3,2,None ,4,4,0,-6, None,-5]
    print(minDepth2(build_tree_inorder(inp5)))
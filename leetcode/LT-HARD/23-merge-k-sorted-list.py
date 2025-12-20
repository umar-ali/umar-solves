from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#-------helper funcs---------
def build_linked_list(*elems):
    h = None
    prev = None
    for e in elems:
        n = ListNode(e)
        if h is None:
            h = n
            prev = n
        else:
            prev.next = n
            prev = n
    return h

def print_ll(h:ListNode | None):
    while h is not None:
        print(h.val, end="")
        if h.next is not None:
            print(", ", end="")
        else:
            print()
        h = h.next
#-------------------------------

def merge_sorted_pair(p:Optional[ListNode], q:Optional[ListNode])  -> Optional[ListNode]:
    if p is None:
        return q
    elif q is None:
        return p
    out = None
    last = out
    while p is not None and q is not None:
        small = None
        if p.val < q.val:
            small = p
            p = p.next
        elif p.val >= q.val :
            small = q
            q = q.next
        if out is None:
            out = small
            last = out
        else:
            last.next = small
            last = small
        
    
    if p is None:
        last.next = q
    elif q is None:
        last.next = p
    return out
            


def mergeKLists(lists:list[Optional[ListNode]]) -> Optional[ListNode]:
    n = len(lists)
    m = n//2
    if n==0:
        return None
    elif n==1:
        return lists[0]
    # lists.sort(key=lambda node: node.val if node is not None else node)
    return merge_sorted_pair(mergeKLists(lists[:m]), mergeKLists(lists[m:n]))

if __name__ == "__main__":
    # l1 = build_linked_list(1,4,5)
    # l2 = build_linked_list(1,3,4)
    # print_ll(merge_sorted_pair(l1, l2))
    raw_input = [[1,4,5],[1,3,4],[2,6]] 
    input_list = []
    for l in raw_input:
        input_list.append(build_linked_list(*l))
    out = mergeKLists(input_list)
    print_ll(out)


    raw_input = [[],[],[]] 
    input_list = []
    for l in raw_input:
        input_list.append(build_linked_list(*l))
    out = mergeKLists(input_list)
    print_ll(out)
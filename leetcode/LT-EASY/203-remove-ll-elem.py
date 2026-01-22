from typing import Optional

class ListNode:
    def __init__(self, val=0, next = None):
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


def removeElements(head:Optional[ListNode], val:int) -> Optional[ListNode]:
    curr = head
    prev = None
    print(head.val)
    while curr is not None:
        if curr.val == val:
            if prev is None:
                head = curr.next
            else:
                prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head

if __name__ == "__main__":
    l1 = build_linked_list(*[1, 2, 3, 4, 2])
    print_ll(l1)
    l1_ans =removeElements(l1, 2)
    print_ll(l1_ans)
    



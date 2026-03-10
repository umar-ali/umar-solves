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


def reorderList(head:Optional[ListNode]) -> None:
    ...


if __name__ == "__main__":
    ll = build_linked_list(*[1,2,3,4,5])
    reorderList(ll)
    print_ll(ll)
    

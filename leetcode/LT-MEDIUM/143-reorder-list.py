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
    # find the middle
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    h2 = slow.next
    slow.next = None # made the the end end

    # reverse from middle
    t1 = None
    t2 = None

    while h2:
        t2 = h2.next
        h2.next = t1
        t1 = h2
        h2= t2

    # merge them
    ptr = head
    tmp = t1
    while tmp:
        #store next
        nxt_ptr = ptr.next
        nxt_h2 = tmp.next


        #attach
        ptr.next = tmp
        tmp.next = nxt_ptr

        #set for next iteration
        ptr = nxt_ptr
        tmp = nxt_h2


if __name__ == "__main__":
    ll = build_linked_list(*[1,2,3,4,5])
    print_ll(ll)
    reorderList(ll)
    print_ll(ll)
    

from typing import Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def removeNthfromEnd(head:Optional[ListNode], n:int) -> Optional[ListNode]:
    #Find mid
    # - use hare and tortoise?
    # t = head
    # if t is None:
    #     return None
    # h = head.next
    # m = 1
    # yo = 0
    # while h is not None:
    #     i = 0
    #     while h is not None and i < m:
    #         yo = 1
    #         h = h.next
    #         i+=1
    #     m += 1
    #     t = t.next
    #calculate size and pos and choose whether to start from head or mid
    # sz = (2 ** yo) * m

    ptr = head
    sz = 0
    while ptr is not None:
        sz+=1
        ptr = ptr.next

    pos = sz - n

    if pos == 0:
        head = head.next
        return head

    # elif pos >= m:
    #     pos -= m
    #     st = t #start from mid

    # else:
    #     st = head #start from head

    #have two pointer prev and curr
    # if curr is at pos, connect prev. next to curr.next 
    # handle if n is at head or tail...?

    prev = None
    curr = head 
    while pos > 0 :
        prev = curr
        curr = curr.next
        pos -= 1

    prev.next = curr.next
    return head

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

if __name__ == "__main__":
    h = build_linked_list(1)
    print_ll(h)
    rh = removeNthfromEnd(h, 1)
    print("ans", end="->")
    print_ll(rh)
    print()


    h = build_linked_list(1, 2)
    print_ll(h)
    rh = removeNthfromEnd(h, 1)
    print("ans", end="->")
    print_ll(rh)

    h = build_linked_list(1, 2, 3, 4)
    print_ll(h)
    rh = removeNthfromEnd(h, 1)
    print("ans", end="->")
    print_ll(rh)

    h = build_linked_list(1, 2, 3, 4)
    print_ll(h)
    rh = removeNthfromEnd(h, 2)
    print("ans", end="->")
    print_ll(rh)

    h = build_linked_list(1, 2, 3, 4, 5)
    print_ll(h)
    rh = removeNthfromEnd(h, 2)
    print("ans", end="->")
    print_ll(rh)






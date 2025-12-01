class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def swapPairs(head:ListNode | None = None) -> ListNode | None:
    if head is None:
        return None
    new_head = None
    tail = None
    curr = head

    while curr is not None and curr.next is not None:
        next = curr.next.next
        #swap_pairs

        p1 = curr.next
        p2 = curr
        p2.next = None
        p1.next = p2

        if new_head is None:
            new_head = p1
        else:
            tail.next = p1
        tail = p2
        curr = next

    if curr is not None and curr.next is None:
        if new_head is None:
            new_head = curr
        elif tail is not None:
            tail.next = curr
    return new_head


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
    l1 = build_linked_list(1, 2, 3, 4)
    print_ll(l1)
    l1_s = swapPairs(l1)
    print_ll(l1_s)

    l1 = build_linked_list(1, 2, 3, 4, 5)
    print_ll(l1)
    l1_s = swapPairs(l1)
    print_ll(l1_s)


    l1 = build_linked_list(1)
    print_ll(l1)
    l1_s = swapPairs(l1)
    print_ll(l1_s)

    l1 = build_linked_list(None)
    print_ll(l1)
    l1_s = swapPairs(l1)
    print_ll(l1_s)











class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


#-------helper funcs---------
def build_linked_list_with_cycle(elems:list[int], pos:int = -1):
    h = None
    prev = None
    cycled = None
    for i, e in enumerate(elems):
        n = ListNode(e)
        if h is None:
            h = n
            prev = n
        else:
            prev.next = n
            prev = n

        if i == pos:
            cycled = n
        if i == len(elems) - 1:
            n.next = cycled
    
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


def hasCycle(head: ListNode | None) -> bool:
    
    tort = head
    hare = head

    while tort and hare and hare.next:
        tort = tort.next
        hare = hare.next.next

        if tort == hare:
            return True
    return False


if __name__ == "__main__":
    ll1 = build_linked_list_with_cycle([3, 2, 0, -4], -1)
    print(hasCycle(ll1))

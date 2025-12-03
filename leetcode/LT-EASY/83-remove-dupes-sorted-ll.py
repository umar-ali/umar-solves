
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



def deleteDuplicates(head:ListNode | None = None) -> ListNode | None:
    prev = None
    curr = head
    while curr is not None:
        if prev is not None and curr.val == prev.val:
            #skipping duplicates, attaching it's next to it's previous
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head

if __name__ == "__main__":
    l1 = build_linked_list(None)
    print_ll(l1)
    l1_ans = deleteDuplicates(l1)
    print_ll(l1_ans)

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


def reverseKGroup(head:Optional[ListNode], k:int) -> Optional[ListNode]:
    if head is None:
        return None

    curr = head
    new_head = None
    tail = None
    while curr is not None:
        group_head = curr #before reversing
        count = 0
        prev = None
        next_node = None

        while curr is not None and count < k:
            #linked list reverse
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count+=1

        #Handling lif last group is not complete
        if count != k:
            #re-reverse last segment
            curr = prev
            next_node = None
            last = None
            while curr is not None:
                #linked list reverse
                next_node = curr.next
                curr.next = last
                last = curr
                curr = next_node
            prev = last

        #if you think, prev is head of reversed ll
        if new_head is None:
            new_head = prev

        #connecting reversed segment to alread processed ll
        #so, head of reversed segment(prev) to 
        if tail is not None:
            tail.next = prev

        tail = group_head
    return new_head


if __name__ == "__main__":
    elems = [1,2,3,4,5]; k = 3
    ll = build_linked_list(*elems)
    print_ll(ll)
    n_ll = reverseKGroup(ll, k)
    print_ll(n_ll)
    elems = [1,2,3,4,5,6]; k = 3
    ll = build_linked_list(*elems)
    print_ll(ll)
    n_ll = reverseKGroup(ll, k)
    print_ll(n_ll)
    elems = [1,2]; k = 2
    ll = build_linked_list(*elems)
    print_ll(ll)
    n_ll = reverseKGroup(ll, k)
    print_ll(n_ll)





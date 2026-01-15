class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


#-------helper funcs---------
def build_linked_list_with_intersection(intersectVal, listA, listB):
    headA = None
    prevA = None
    intersectNode = None
    for i, e in enumerate(listA):
        n = ListNode(e)
        if headA is None:
            headA = n
            prevA = n
        else:
            prevA.next = n
            prevA = n
        if e == intersectVal:
            intersectNode  = n

    headB = None
    prevB = None

    for i, e in enumerate(listB):

        if e == intersectVal:
            prevB.next = intersectNode
            break

        n = ListNode(e)
        if headB is None:
            headB = n
            prevB = n
        else:
            prevB.next = n
            prevB = n

    return headA, headB



def print_ll(h:ListNode | None):
    while h is not None:
        print(h.val, end="")
        if h.next is not None:
            print(", ", end="")
        else:
            print()
        h = h.next
#-------------------------------


def reverse(head: ListNode | None) -> ListNode | None:
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next 
    return prev


def _get_intersection_node(headA: ListNode | None, headB: ListNode | None) -> ListNode | None :
    # use floyd's cycle detection
    # faster but modifies 
    if headA is None or headB is None:
        return None

    revB = reverse(headB)

    t = headA
    while t.next:
        t = t.next
    t.next = revB #modification!!!

    

    fast = headA
    slow = headA
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = headA

            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None

#TODO: find middle ground b/w two

def get_intersection_slow(headA: ListNode | None, headB: ListNode | None) -> ListNode | None :
    #naive O(n x m) approach
    #TLE
    if headA is None or  headB is None:
        return None
    
    ptrA = headA

    while ptrA:
        ptrB = headB
        while ptrB:
            if ptrA == ptrB:
                return ptrA
            ptrB = ptrB.next
        ptrA = ptrA.next
    return None

def len(head: ListNode | None) -> int:
    ln = 0
    t = head

    while t:
        t = t.next
        ln += 1
    return ln

def get_intersection(headA: ListNode | None, headB: ListNode | None) -> ListNode | None :
    #naive O(n x m) approach
    #TLE
    if headA is None or  headB is None:
        return None
    ln_a = len(headA)
    ln_b = len(headB)

    #find the max and difference:
    if ln_a < ln_b:
        ptr_mx = headB
        ptr_mn = headA
        d = ln_b - ln_a
    else:
        ptr_mx = headA
        ptr_mn = headB
        d = ln_a - ln_b

    for i in range(d):
        ptr_mx = ptr_mx.next

    while ptr_mx and ptr_mn and ptr_mx != ptr_mn:
        ptr_mx = ptr_mx.next
        ptr_mn = ptr_mn.next

    return ptr_mx

if __name__ == "__main__":
    la = [1, 2, 3, 4]
    lb = [5,6, 3, 6]
    ival = 3
    lla, llb = build_linked_list_with_intersection(ival, la, lb)

    inter = get_intersection(lla, llb)
    if inter:
        print(inter.val)
    else:
        print(inter)

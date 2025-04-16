class Node:
    value:int
    next:"Node"
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
    
    @staticmethod
    def build(values:list):
        l = len(values)
        n = Node(values[0])
        head = n
        for i in range(1, l):
            n.next = Node(values[i])
            n = n.next
        return head
    
    @staticmethod
    def extend(a: "Node", b: "Node"):
        head = a
        while a.next != None:
            a = a.next
        a.next = b
        return head
    
    def show(a:"Node"):
        while True:
            if a.next == None:
                print(a.value)
                break
            print(a.value, end="->")
            a = a.next
            
    
def solve(linkA, linkB):
    #floyd cycle detection
    #two pointer going in different pace..eventually meet if cycle
    tempA = linkA
    tempB = linkB
    while(tempA != tempB):
        if tempA == None:
            tempA = linkB
        if tempB == None:
            tempB = linkA
        tempA = tempA.next
        tempB = tempB.next
    return tempA.value


if __name__ == "__main__":
    #la = [4, 1, 8, 4, 5]
    #lb = [5, 6, 1, 8, 4, 5]
    #lc = [8, 4, 5]
    #intVal = 8
    a = Node.build([4, 1])
    b = Node.build([5, 6, 1])
    c = Node.build([8, 4, 5])
    la = Node.extend(a, c)
    lb = Node.extend(b, c)
    Node.show(la)
    Node.show(lb)
    print(solve(la, lb))
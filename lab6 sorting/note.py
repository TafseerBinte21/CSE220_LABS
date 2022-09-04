class DoublyList:
    def __init__(self, a=None):
        self.head = Node(None, None, None)
        tail = self.head
        for i in a:
            n = Node(i, None, None)
            tail.next = n
            n.prev = tail
            tail = tail.next
        tail.next = self.head
        self.head.prev = tail
class Node:
    def __init__(self, element, next, prev):
        self.element = element
        self.next = next
        self.prev = prev

class DoublyList:
    def __init__(self,a):
        self.head = Node(a[0],None,None)
        tail = self.head

        for i in range(1, len(a)):
            newnode = Node(a[i],None,None)
            newnode.prev = tail
            tail.next = newnode
            tail = tail.next
            
    
    def showList(self):
        if self.head==None:
            print("empty list")
        else:
            showing = " "
            show = self.head
            while(show!=None):
                showing += "<-- "+str(show.element)+" -->"
                show =  show.next
            print(showing)


def insertionSort(self):
    i = self.head.next
    while i!=None:
        sort = i
        while i.prev.element > i.element:
            i.element, i.prev.element = i.prev.element, i.element
            
            i = i.prev
            if i.prev==None:
                i=sort
                break
        i = i.next 



d=DoublyList([5,6,9,2,1])
insertionSort(d)
d.showList()

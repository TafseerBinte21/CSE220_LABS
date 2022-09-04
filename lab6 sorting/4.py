class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

    
class MyList:
    def __init__(self,a= None):
        if a==None:
            self.head = None
        elif isinstance(a,list):
            head = None
            tail = None
            for i in a:
                node1 = Node(i,None)
                if head is None:
                    head = node1
                    tail = node1

                else:
                    tail.next = node1
                    tail =tail.next
            self.head = head
            
        elif isinstance(a,MyList):
            n=a.head
            head = None
            tail = None
            while n!=None:
                
                node1 = Node(n.element,None)
                if head==None:
                    head = node1
                    tail = node1

                else:
                    tail.next = node1
                    tail = node1
                n=n.next
            self.head = head


    def showList(self):
        if self.head== None:
            print("empty list")
        else:
            showing = " "
            show = self.head
            while(show!=None):
                showing += str(show.element)+">"
                show =  show.next
            print(showing)


def selectionSort(self):
    i = self.head
    while i.next.next!=None:
        min = i
        q = i.next
        while q.next:
            if q.element < min.element:
                min = q
            q = q.next

        i.element, min.element = min.element,i.element
        i = i.next

a=[2,5,6,1,9]
li = MyList(a)
selectionSort(li)
li.showList()

        
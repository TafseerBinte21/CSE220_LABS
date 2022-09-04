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

        

def bubbleSort(self):
    swap = True
    while swap:
        swap = False
        sort = self.head
        while sort.next!= None:
            q = sort.next
            if sort.element > q.element:
                temp = sort.element
                sort.element = q.element
                q.element = temp
                swap = True
            sort = sort.next
        
      
a=[2,5,6,1,9]
li = MyList(a)
bubbleSort(li)
li.showList()
   


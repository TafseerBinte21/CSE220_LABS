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

    def isEmpty(self):
            if self.head!=None:
                return False
            else:
                return True

    def clear(self):
            while self.head!=None:
                head = self.head
                self.head=self.head.next
                head=None
        
    def insertElement(self,newElement,index=None):
        c = self.head
        while c!=None:
            if c.element==newElement:
                return
            c =c.next
        if index == None:
            node = Node(newElement,None)
            if self.head== None:
                self.head = node
                return
            else:
                tail = self.head
                while tail.next!=None:
                    tail=tail.next
                tail.next = node


            return
       
        size = 0  
        i = self.head
        while i!=None:
               i=i.next
               size+=1
        if index <0 or index > size:
            print("inavlid index")
            return
        else:
            if index == 0:
                node=  Node(newElement,self.head)
                node.next = self.head
                self.head = node
            else:
                node = Node(newElement,None)
                i = self.head
                c = 0
                while i!=None:
                    c+=1
                    if c==index:
                        break
                    i = i.next
                temp = i.next
                i.next=node
                node.next=temp

    def remove(self,deletekey):
        b = self.head
        if b!=None:
            if b.element == deletekey:
                self.head = b.next
                b = None
                return deletekey
            



a = MyList()
b = MyList([1,2,3,4,4])
b.insertElement(6)
b.showList()
print("6. def insertElement(self, newElement, index)")
b.insertElement(7,2)
b.showList()
b.remove(1)
b.showList()
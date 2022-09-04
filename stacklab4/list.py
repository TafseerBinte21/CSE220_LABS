class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

class stacklist:
    def __init__(self):
        self.head = None

    def push(self,element):
        if self.head is None:
            self.head = Node(element,None)
        else:
            nNode = Node(element,self.head)
            self.head = nNode

    def peek(self):
        if self.head==None:
            return None
        return (self.head.value)
    
    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.value


def bracketbalance(expression):
    openbracket=["[","{","("]
    closingbracket=["]","}",")"]
    equation=stacklist()
    
    for i in expression:
        if i in openbracket:
            equation.push(i)
        elif i in closingbracket:
            if equation.peek() == None:
                print("expression is not correct")
                count = 0
                for j in expression:
                    if j == i:
                        break
                    count += 1
                print("Error at character #",count+1,". ‘",i,"‘- not opened")
                return
            
            stop = equation.pop()
            a=openbracket.count(stop)
            b=closingbracket.count(i)
            if a != b:
                print("expression is not correct")
                count = 0
                for j in expression:
                    if j == stop:
                        break
                    count += 1
                print("Error at character #",count+1,". ‘",stop,"‘- not closed")
                return
    
    if equation.peek() is not None:
        print("expression is not correct")
        count = 0
        for j in expression:
            if j == stop:
                break
            count += 1
        print("Error at character #",count+1,". ‘",stop,"‘- not closed")
        return
    else:
        print("expression is correct")
        return

bracketbalance("1+[{2+*3/4)}]")

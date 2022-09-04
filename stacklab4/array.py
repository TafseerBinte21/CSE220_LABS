class arrayStack:
    stack =[]
    p =-1
    def push(self,element):
        self.stack+=[element]
        self.p+=1
    
    def peek(self):
        if self.p==-1:
            return None
        return(self.stack[self.p])
        

    def pop(self):
        v = self.stack[self.p]
        self.stack = self.stack[:-1]
        self.p-=1
        return v


def bracketbalance(expression):
    openbracket=["[","{","("]
    closingbracket=["]","}",")"]
    equation=arrayStack()
    
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

bracketbalance("1+2*(3/4)")
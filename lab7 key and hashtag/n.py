class keyIndex:
    k=[]
    def __init__(self,a):
        neg = False
        self.max = a[0]
        self.min = a[0]
        self.givenArray = a

        for i in range(len(a)):
            if a[i] > self.max:
                self.max = a[i]
            elif a[i] < self.min:
                self.min= a[i]
                
        if self.min < 0:
            neg = True
               
        if neg:
            self.min = self.min*(-1)
        
        if not neg:
            k=[0]*(self.max+1)
        else:
            k=[0]*(self.max+self.min+1)

        
        for i in range (len(a)):
            if neg:
                k[a[i]+self.min]+=1
            else:
                k[a[i]]+=1
       
        
        self.k = k
        
    def searching(self,value):
        if value < self.min or value > self.max:
            return False
        if self.k[value+self.min]==0:
            print("l")
            return True
        else:
            return False

    def sorting(self):
        index = 0
        for i in range (len(self.k)):
            temp = self.k[i]
            while temp!=0:
                temp-=1
                self.givenArray[index]=i-self.min
                index+=1
        
        return self.givenArray
           
   
t=[-5,4,7,7,3,2,1]
b=keyIndex(t)
c=b.searching(100)
print(c)
print(b.sorting())


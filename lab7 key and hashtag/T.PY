class KeyIndex:
    def __init__(self,a):
        self.temp3=0
        for i in range(len(a)):
            if a[i]<0:
                z=myMin(a)
                self.temp3=z*(-1)
                for i in range(len(a)):
                    a[i]+= self.temp3 
            break 
        print(a)



        temp=myMax(a)
        temp2=temp+1
        self.k=[0]*temp2
        print(self.k)

        for i in range(len(a)):
                    self.k[a[i]]+=1
        print(self.k)

    def sort(self):
        for j in range(len(self.k)):
            if self.k[j]!=0:
                    for i in range(self.k[j]):
                        print(j-self.temp3)

    def search(self,inp):
        z=self.temp3+inp
        for i in range(len(self.k)):
            if self.k[i]>0:

                # if self.k[i]==z:
                #     return True
                # else:
                #     return False


                if self.k[z]!=0:
                    return True
                else:
                    return False
def myMax(a):

    maxm = a[0]


    for x in a:

        if x > maxm :
            maxm=x
    return maxm
def myMin(a):

    minm = a[0]


    for x in a:
        if x < minm :
             minm = x
    return minm

a=[-6,0,2,4,1,-7,3,8]
b=KeyIndex(a)
b.sort()
print(b.search(1))
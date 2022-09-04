def bubbleSort(a):
    
    swap = True
    while swap:
        swap = False
        for i in range (0,len(a)-1):
            if a[i]> a[i+1]:
                swap = True
                a[i],a[i+1] = a[i+1],a[i]
                

    return a

a=[5,6,7,2,1]
bubbleSort(a)

for i in range(len(a)):
    if i== len(a)-1:
        print(a[i])
    else:
        print(a[i],end=",")
  


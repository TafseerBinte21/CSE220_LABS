def intersection(circle1,start1,size1,circle2,start2,size2):
    ind1 = start1
    ind2 = start2

    c1=len(circle1)
    c2=len(circle2)

    lineararray = [0]*size1
    k = 0

    for i in range(size1):
        ind2 = start2
        for j in range(size2):
            if circle1[ind1] == circle2[ind2]:
               
                lineararray[k]=circle2[ind2]
                k+=1
              
            ind2 = (ind2+1)%c2
        ind1 = (ind1+1)%c1

    
    common=[0]*k
    for i in range(k):
        common[i]=lineararray[i]
    return(common)
    
print(intersection([40,50,0,0,0,10,20,30],5,5,[10,20,5,0,0,0,0,0,5,40,15,25],8,7))

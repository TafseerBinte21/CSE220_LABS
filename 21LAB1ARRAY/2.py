def rotateLeft(source,k):
    for i in range(0,k):
        firstt = source[0] 
                                                                              
        for j in range(0,len(source)-1):
            source[j]=source[j+1]
    
        source[len(source)-1] = firstt
    

a = ["P","E","A","T","N","I","B","R","E","E","S","F","A","T"]


rotateLeft(a,4)
print(a)

                                                                                                                                                                                                                                                                                                 
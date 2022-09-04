def arraySplit(A):
    leftPansum = 0
    rightPansum = 0
    
    for i in range(len(A)):
        leftPansum = 0
        rightPansum = 0

        for j in range(0,i+1):
            leftPansum+=A[j]
        for j in range(i+1, len(A)): 
            rightPansum+= A[j]
        
        
        if leftPansum == rightPansum:
            return True
            
        
    return False

A = [1,1,1,3,2,1]
print (arraySplit(A)) 



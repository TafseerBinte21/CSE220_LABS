def palindromecircular(circular,start,size):
   
    len1 = len(circular)
    ind=start

    c = 0
    for i in range(0,size//2):
        if circular[ind] != circular[(size+start-1)%len1]:
            c = 1
            break
        i+=1
    
    
    if c==1:
        print('False')
    else:
        print('True')
             

circular =  [20,10,0,0,0,10,20,30]
start = 5
size = 5
palindromecircular(circular,start,size)
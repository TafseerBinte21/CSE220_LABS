def array(n):
    li = [0]*n*n
    a = 0
    part = 1

    for i in range(len(li)):
        
        if a >= n - part:
            li[i] =n-a
            
        a+=1
        if a==n:
            a = 0
            part+=1
    print(li)
    

array(3)                
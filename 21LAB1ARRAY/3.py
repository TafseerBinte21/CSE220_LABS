def remove(source,size,idx):
    for i in range(len(source)):
        i = idx
        if i < size: 
            source[i]=source[i+1]
            idx+=1
        else:
            size-=1
source=[10,20,30,40,50,0,0]
remove(source,5,2)
print(source)
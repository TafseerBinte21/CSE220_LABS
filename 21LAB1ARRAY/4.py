def removeAll(source,size,element):
    c = 0
    for i in range(len(source)):
        if source[i] == element:
            source[i] = 0
            c += 1
    i = 0
    while i < size - c :
        if source[i] == 0:
            
            for j in range (i,len(source)-1):
                source[j] = source[j+1]
            source[len(source)-1] = 0
        else:
            i += 1
    return source


source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)

print(source)


def shiftLeft(source,k):
    for i in range(0,len(source)-k):
        source[i]=source[i+k]
    for i in range(len(source)-k):
        source[i+k] = 0
a = [10,20,30,40,50,60]
shiftLeft(a,3)
print(a)



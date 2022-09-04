def maxbunch(array):
    c = 1
    a = 1
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            c +=1
        else:
            c=1

    if c > a:
        a = c

    return a

array = [1,1,2, 2, 1, 1,1,1]
print (maxbunch(array)) 

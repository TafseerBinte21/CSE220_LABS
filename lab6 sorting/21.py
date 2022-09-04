def insertionSort(array):
    for i in  range(1,len(array)):
        sort = array[i]
        

        while array[i-1]> sort and i>0 :
           array[i],array[i-1]= array[i-1],array[i]
           i-=1
           
    return array

a=[5,6,9,2,1]
print(insertionSort(a))


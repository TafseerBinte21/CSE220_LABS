def insertionSortRecursive(array,i):
    
    if i == len(array):
        return

    if i < len(array):
        j = i-1
        sort = array[i]
      
        while j>=0 and array[j]>sort:
           array[j+1],sort= array[j],array[j+1]

           j-=1
         
        insertionSortRecursive(array,i+1)

array=[5,6,7,2,1]
i=1
insertionSortRecursive(array,i)
print(array)

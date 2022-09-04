def insertionSortRecursive(array,i):
    
    if i == len(array):
        return

    if i < len(array):
        j = i-1
        sort = array[i]
      
        while j>=0 and array[j]>sort:
           array[j+1]= array[j]

           j-=1
        array[j+1]= sort   
        insertionSortRecursive(array,i+1)

array=[5,6,7,2]
i=1
insertionSortRecursive(array,i)

for i in range(len(array)):
    if i== len(array)-1:
        print(array[i])
    else:
        print(array[i],end=",")
  


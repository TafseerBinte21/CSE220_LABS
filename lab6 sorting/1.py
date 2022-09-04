def sortarrayRecursive(array,index,j):
    
    if index == len(array)-1 and j == len(array)-1:
        return array

    if index < len(array):
        min = index

        if j < len(array):
            if array[j] < array[min]:
                min = j

            sortarrayRecursive(array,min,j+1)

        if min != index:
            array[min],array[index]=array[index],array[min]
        
        sortarrayRecursive(array,index+1,j+1)


array=[15,3,2,4,12,5]
index = 0
j=index+1
sortarrayRecursive(array,index,j)

for i in range(len(array)):
    if i== len(array)-1:
        print(array[i])
    else:
        print(array[i],end=",")
  



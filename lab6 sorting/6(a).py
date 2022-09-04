def binarySearch(array,l,r,element):
    if not l < r:
        return -1
        
    midpoint = (l+r)//2
   
        
    if array[midpoint]<element:
        return binarySearch(array,midpoint+1,r,element)
        
            
    elif array[midpoint] > element:
        return binarySearch(array,l,midpoint,element)
            
    else:
        return midpoint
            

  
a= [1,2,3,4,5,5]
l = 0
r = len(a)
element = 5
print(binarySearch(a,l,r,element))


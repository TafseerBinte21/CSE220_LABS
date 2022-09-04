def binarySearch(array,l,r,element):
    if l<=r:
        
        midpoint = (l+r)//2
        mid = array[midpoint]
        
        if element==mid:
            return mid
            
        elif element > mid:
            return binarySearch(array,midpoint+1,r,element)
            
        else:
            return binarySearch(array,l,midpoint-1,element)

    else:
        return "element is not found"
            
    

a= [5,1,2,3,4,5]
l = 0
r = len(a)-1
element = 15
print(binarySearch(a,l,r,element))




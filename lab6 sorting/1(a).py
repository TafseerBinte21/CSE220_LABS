def selection_sort(a,i,j):

  l=len(a)
  if i == l and j==l:

    return -1

  if i < l-1:

    min=i

    while j < l:

      if a[j] < a[min]:

        min = j

      j=j+1

    if min != i:

      temp=a[i]

      a[i]=a[min]

      a[min]=temp

    selection_sort(a,i+1,i+2)

A=[1,7,17,15,3,9,10,0,25,6]

i=0

j=i+1

selection_sort(A,i,j)
print(A)

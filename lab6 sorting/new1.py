def nthfibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return nthfibonacci(n-1)+nthfibonacci(n-2)

a={}
def fibmemo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
      if n in a.keys():
        return a[n]
      a[n]= a[n]= fibmemo(n-1)+fibmemo(n-2)
      return a[n]
        

n=100
print(fibmemo(n))

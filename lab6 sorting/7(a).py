a=[0]*2000 #i am not understanding array ta kibhabe nibo

def nthfibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return nthfibonacci(n-1)+nthfibonacci(n-2)

def fibmemo(n):
    if a[n] > 0:
        return a[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a[n]= fibmemo(n-1)+fibmemo(n-2)
        return a[n]
        

n=9
print(fibmemo(n))

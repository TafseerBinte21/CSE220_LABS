class fib:
    a = []
    def nthfibonacci(self,n,f=True):
        if len(fib.a) < n and f:
            fib.a = [0]*(n+1)

        if fib.a[n] > 0:
            return fib.a[n]
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            fib.a[n]=self.nthfibonacci(n-1,False)+self.nthfibonacci(n-2,False)
            return fib.a[n]
        

n=9
f = fib()
print(f.nthfibonacci(n))

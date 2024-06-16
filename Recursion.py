#direct recursion:

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))

#indirect recursion:

def a(n):
    if n>0:
        return b(n-1) 
    else:
        return True
def b(n):
    if n>0:
        return a(n-1)
    else:
        return False
print(a(5))

# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))














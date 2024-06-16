def fabon(n):
    if n<=1:
        return n
    else:
        return (fabon(n-1)+fabon(n-2))
n=int(input("Enter your n value:"))
if n<=0:
    print("enter +ve integer")
else:
    for i in range(0,n):
        print(fabon(i))

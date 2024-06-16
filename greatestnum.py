#METHOD-1
a, b, c = map(int, input("Enter three numbers: ").split())
if (a >= b & a >= c):
    print(a," is the greatest number.")
elif (b >= c):
    print(b," is the largest number.")
else:
    print(c,"is the largest number.")

#METHOD-2
a, b, c = map(int, input("Enter three numbers: ").split())
if (a >= b and a >= c):
    print(a," is the largest number.")
elif ( b >= c):
    print(b," is the largest number.")
else:
    print(c,"is the largest number.")




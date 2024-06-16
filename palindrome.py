
n= int(input())
temp=n
def integer(n):
    res = 0
    while n!=0:
        r=n%10
        res = ((res*10)+r)
        n =n//10
    return res
result=integer(n)
if result== temp:
    print("yes Palindrome")
else:
    print("not a Palindrome")




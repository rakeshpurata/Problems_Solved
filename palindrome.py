# string=input()
# def palindrom(string):
#     half=len(string)//2
#     print(half)
#     if len(string)%2==0:
#         first_string= string[:half]
#         second_string=string[half:]
#     else:
#         first_string=string[:half]
#         second_string=string[half+1:]
#     if first_string == second_string[::-1]:
#       print('palindrome')
#     else:
#         print('not a palindrome')
# print(palindrom(string))



# def palindrom(s):
#     if s==s[::-1]:
#         return True
#     else:
#         return False
# s=input()
# if palindrom(s):
#     print("YES")
# else:
#     print("No")

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




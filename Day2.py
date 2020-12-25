#odd numbers
# for i in range(1,20,2):
#     print(i)

# #Reverse odd numbers
# for i in range(19,0,-2):
#     print(i)

#Sum of n num
# n=int(input())
# c=0
# for i in range(1,n+1):
#     c+=i
# print(c)

#  factorial
# n=int(input())
# c=1
# for i in range(1,n+1):
#     c*=i
# print(c)

# swapping of numbers
# a,b=5,10
# print(a)
# print(b)
# a,b=b,a
# print(a)
# print(b)

# nested loop
# for i  in range(5):
#     for j in range(i+1):
#         print(i,end='',sep=' ')
#     print()

# '''
# n=5
# *****
# *****
# *****
# *****
# *****
# '''
# n=int(input())
# for i in range(n):
#     for j in range(n):
#         print("*",end='')
#     print()

# '''
# n=4
# *
# **
# ***
# ****
# '''
# for i in range(0,int(input())):
#     for j in range(i+1):
#         print("* ",end='')
#     print()

# '''
# string manipulation
# '''
# for i in range(int(input())):
#     print("* "*(i+1))

'''
Break and continue statements
'''

# for i in range(0,10):
#     if i%2!=0:
#         continue #loop skipping statement....all other statements in the loop will NOT be executed
#     if i>7:
#         break #'current'loop exiting statement
#     print(i)

# prime num 
# n=int(input())
# is_prime=True
# for i in range(2,n): #[2,n-1]:
#     if n%i==0: #n is multiple of i 
#         is_prime=False
#         break
# if is_prime:
#     print("Prime Number")
# else:
#     print("Not Prime Number")      

# optimised prime
# n=int(input())
# nw=int(n**0.5)
# is_prime=True
# for i in range(2,nw+1): #[2,n-1]:
#     if n%i==0: #n is multiple of i 
#         is_prime=False
#         break
# if is_prime:
#     print("Prime Number")
# else:
#     print("Not Prime Number")      

# nCr 
"""
n!/r!(n-r)!
"""
n=int(input())
r=int(input())
nr=n-r

fact_n,fact_r,fact_nr=1,1,1
for i in range(1,n+1):
    fact_n*=i

for i in range(1,r+1):
    fact_r*=i

for i in range(1,nr+1):
    fact_nr*=i

ans=fact_n/(fact_r*fact_nr)
print(ans)
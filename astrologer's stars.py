''' 27.9.20-28.9.20
author-manas verma
astrologer's stars

specs

1. You have to take an integer type variable, and the input of the variable will define the
 length of the triangle.
2. You have to declare another Boolean variable.
3. When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
4. But if the value of Boolean is 0 or false, then the triangle will be printed upside down.


# Pattern Printing
# Input = Integer n
# Boolean = True or False
0=false
1=true
#
# True
# *
# **
# ***
# ****
#
# False
# ****
# ***
# **
# *
'''
print("welcome to astrologer's stars")
a = int(input("enter the number of lines of stars you want:"))
b = int(input("pls enter 0 or 1:"))
c = bool(b)
if c==True:
    for i in range(1,a+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif c==False:
    for i in range(1,a-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
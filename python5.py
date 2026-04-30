#patterns
num =4
i=1
while i<=num:
    j=1
    while j<=num:
        print("*",end="")
        j+=1
    print()
    i+=1    
#**** **** **** ****    

#-----------------------------------------

num=4
i=1
while i<=num:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1    
#* ** *** ****

#------------------------------------------

n=5
for i in range(n):
    print("*"*i)
#* ** *** ****

#-----------------------------------------

num=4
i=1
while i<=num:
    j=1
    while j<=num:
        print(i,end="")
        j+=1
    print()
    i+=1    
#1111 2222 3333 4444

#------------------------------------------

num=4
i=1
while i<=num:
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    print()
    i+=1    
#1 22 333 4444

#----------------------------------------------

num=4
i=1
while i<=num:
    j=1
    while j<=num:
        print(chr(64+i),end="")
        j+=1
    print()
    i+=1    
#AAAA BBBB CCCC DDDD

#----------------------------------------------

n = 4
i = n

while i > 0:
    print("*" * i)
    i -= 1   # decrease by 1#
#**** *** ** *

#----------------------------------------------

n=4
for i in range(n,0,-1):
    print("*"*i)
    
#**** *** ** *

#----------------------------------------------

n = 4
i = 1

while i <= n:
    k = 1
    while k <= n - i:
        print(" ", end="")   # print spaces
        k += 1

    j = 1
    while j <= i:
        print("*", end="")   # print stars
        j += 1

    print()   # move to next line
    i += 1
    
    
n = 4
for i in range(1, n + 1):
    for k in range(n - i):
        print(" ", end="")   # spaces

    for j in range(i):
        print("*", end="")   # stars

    print()   # next line

#   * 
#  **
# ***
#****    
#--------------------------------------------------

n=5
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
    
#--------------------------------------------------

n = 5
for i in range(n,0,-1):
    print(" "*(n-i) + "* " * i)
    
#--------------------------------------------------
    
    
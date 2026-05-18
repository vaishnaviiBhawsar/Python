'''23) Plus Star Pattern
          *
          *
    ***
          *
          *
'''

n= int(input("enter number"))
i = 1 

while i<=n:
    print()

    space = 1
    while space <= n-1:
         print(" " ,end=" ")
         space = space+1
    print("*")
    if i==3:
         print("***")
    i=i+1
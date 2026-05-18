'''30) Extended Slanted Star Block
    **
     **
      **
       **
        **
'''
n=int(input("Enter number:"))

i = 1

while i<=n:

    space = 1
    while space < i:
        print(" ", end="")
        space=space+1

    print("**")
    i=i+1
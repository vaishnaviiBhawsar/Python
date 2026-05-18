'''
*
##
***
####
*****
'''


n = int(input("Enter Number"))
i=1
while i<=n:
    print()

    j=1
    while j<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")

        j=j+1
    i=i+1

         
    
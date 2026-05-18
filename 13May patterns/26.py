'''
*
*#
*#*
*#*#
*#*#*
'''

n=int(input("enter num:"))

for i in range (1,n+1):
    print()
    for j in range(1,i+1):
        if j % 2== 0:
            print("#",end=" ")
        else:
            print("*",end=" ")

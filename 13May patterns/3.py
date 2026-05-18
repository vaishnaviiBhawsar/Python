'''

* 
 *
  *
   *
    *
'''
n = int(input("enter number:"))
for i in range(1,n+1):
    print()

    for j in range(1,i+1):
     
        if i == j :  
            print("*", end="")
        else:
            print(" ", end="")

    print()    

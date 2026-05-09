'''8.
enter n6
 654321
  65432
   6543
    654
     65
'''

n = int(input("Enter number"))
i = 1
while i<=n-1:
    print()  
    
    space = 1
    while space <=i:
         print(" " ,end="")
         space = space+1

    j = n
    while j>=i:
        print(j, end="")
        j =j-1

    i =i+1
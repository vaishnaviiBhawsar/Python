'''
7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
'''

n = int(input("Enter Number:"))

i=1

while i<=n:
     
    num = 2 * (i-1)
 
    j = 1 
    while j<i:
       print(num , end=" ")   
       num = num-1
       j+=1

    space =1 
    while space <=n-i: 
        print("_",end=" ")
        space+=1

    print()
    i+=1
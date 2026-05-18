'''7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
'''

n=int(input("Enter number"))

i=1

while i<=n:
  
     num = i*2

     j=1
     while j<=i:
        print(num,end=" ")
        num=num-1
        j=j+1
  
    space =1 
    while space<= n - i:
       print("_", end=" ")
       space = space+1
     
     
   print()
   i=i+1
    
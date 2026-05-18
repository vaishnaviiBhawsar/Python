'''
A
BB
CCC
DDDD
EEEEE
'''

n = int(input("Enter Number"))


for i in range (65,n+65):
    print()

    j = 65
    while j<=i:
      print(chr(i),end=" ")
        j = j+1
        
    i = i+1



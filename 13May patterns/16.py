'''
a
bc
def
ghij
klmno
'''

n = int(input("Enter Number"))


i = 1
k = 97
while i<=n:
     print()
     j = 1
     while j<=i:
         print(chr(k),end=" ")
         j =j+1
         k =k+1
     i =i+1

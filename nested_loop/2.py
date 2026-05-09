'''
2) WAP to print Square, Cube and Square Root of all numbers from 1 to N '''

import math
n = int(input("Enter Number:"))


for num in range(1,n+1):
     square = num*num
     cube = num**3
     root = math.sqrt(num)

     print("Number =", num)
     print("Square=",square)
     print("Cube=",cube)
     print("Square Root=",root)
  
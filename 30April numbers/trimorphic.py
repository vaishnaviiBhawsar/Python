'''
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''

n = int(input("Enter Number "))
cube = n**3
temp = n
while temp>0:
    if cube % 10 != temp % 10 :
       print("Not an Trimorphic Number")
       break 
    cube = cube // 10
    temp = temp // 10
else:
    print("Trimorphic Number")

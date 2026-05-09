'''1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15'''

n=int(input("Enter number: "))
mul=1
i=1
while i<=n:
   
     mul=mul*i
     i=i+1
print(mul)


    

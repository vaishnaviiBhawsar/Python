'''
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12 

Output:
Abundant Number'''

n = int(input("Enter Number = "))
sum = 0 

'''i = i+1
while i<=n:
     if  n % i == 0:
         sum += i
     i = i+1 
if sum > n :
    print("Abundant Number")
else: 
    print("Not an Abundant Number")'''


for i in range ( 1,n+1):
     if  n % i == 0:
         sum += i
if sum > n :
    print("Abundant Number")
else: 
    print("Not an Abundant Number")


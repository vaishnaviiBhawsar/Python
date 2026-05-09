'''
7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32'''

n=int(input("Enter Number:"))
p=int(input("Enter Number:"))
power=1
for i in range (1,n+1):   
    power= n**p
print("Power=",power)
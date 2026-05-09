'''6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''

n=int(input("Enter a Number: "))
temp=n
sum=0

while n>0:
  r=n%10
  sum=sum+r*r*r
  n=n//10
 
if temp==sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")
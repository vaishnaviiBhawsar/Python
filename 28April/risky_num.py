'''
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2'''

n=int(input("Enter Number: "))
i=2
x=0
count=0
while i<n:
   if n%i==0:
     x=1
     break
   i+=1
if x==0:
   print("Not Composite")
else:
   print("Composite")

j=1

while n>=j:
   if n%j==0:
    count+=1
   j=j+1
print("Factors Count =",count)





